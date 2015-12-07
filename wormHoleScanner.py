#!/usr/bin/env python
#coding=utf-8


from optparse import OptionParser
from utility import logger, IP_Generator, global_options
import logging
from multiprocessing.dummy import Pool
import os
import exp
import pkgutil
from json import dumps
from fnmatch import fnmatch



def singleIpScanner(ip):
    logger.debug("Start to scan %s" % ip)

    result = []

    def addIntoResultIfNotNull(val, port):
        #nonlocal result
        if val:
            logger.warn("Found wormhole vuln in %s:%d : %s" % (ip, port, val))
            result.append(val)

    for _, modname, _ in pkgutil.iter_modules(exp.__path__):

        if not fnmatch(modname, global_options.poc_pattern):
            continue

        try:
            poc_module = __import__("exp.%s" %(modname), fromlist=["port", "verify", "protocol"])
        #logger.debug(poc_module)
            port = poc_module.port
        except AttributeError,e:
            logger.error(e, modname)
            raise e
        except ImportError,e:
            logger.error(e, modname)
            raise e

        try:
            ret = None
            if len(port) == 1:
                ret = poc_module.verify(ip)
                addIntoResultIfNotNull(ret, port[0])

            else:
                for p in port:
                        ret = poc_module.verify(ip, p)
                        addIntoResultIfNotNull(ret, p)

        except AttributeError:
            logger.debug("Cannot found verify method in %s module"
                        % modname)
            continue

    return result

def scan(target, threads):
    logger.info("Going to scan %s IPs" % len(target))
    pool = Pool(threads)
    _ = list(pool.imap_unordered(singleIpScanner, target))
    logger.info("Scanning Done.")


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip",
                    help = "target ip to scan")
    parser.add_option("-f", "--file", dest="filename",
                    help="target IPs to scan(will ignore -i option)",
                    metavar="FILE")
    parser.add_option("-v","--verbose", action="store_true", dest="verbose",
                    help="get more verbose output")
    parser.add_option("-V","--Verbose", action="store_true", dest="Verbose",
                    help="get more verbose output")
    parser.add_option("-o", "--output", dest="output",
                        help="output file")
    parser.add_option("-t", "--threads", dest="threads",
                        help="threads number used for scan")
    parser.add_option("-p", "--poc", dest="poc_pattern", default="*",
                    help="specify Poc to scan, use regex")
    (opt, args) = parser.parse_args()

    if not opt.filename and not opt.ip:
        parser.print_help()
        exit(1)

    global_options.poc_patter= opt.poc_pattern

    if opt.verbose:
        logger.setLevel(logging.INFO)
    if opt.Verbose:
        logger.setLevel(logging.DEBUG)

    if opt.output:
        fh = logging.FileHandler(opt.output)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    threads = int(opt.threads) if opt.threads else 50

    targets = []
    if opt.filename:
        with open(opt.filename, "rb") as f:
            for line in f:
                if line.lstrip(" ").startswith("#"):
                    continue

                targets.append(line.strip())
    elif opt.ip:
        targets.append(opt.ip);

    scan(IP_Generator(targets), threads)
