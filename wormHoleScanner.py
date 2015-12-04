#!/usr/bin/env python
#coding=utf-8


from optparse import OptionParser
from utility import logger, IP_Generator
import logging
from multiprocessing.dummy import Pool
import os
import exp
import pkgutil
from collections import defaultdict
from json import dumps

def singleIpScanner(ip):
    logger.info("Start to scan %s" % ip)

    result = []

    for _, modname, _ in pkgutil.iter_modules(exp.__path__)
        poc_module = __import__(modname)
        port = poc_module.port
        if len(port)==1:
            ret = poc_module.verify(ip)
            if ret:
                logger.warn("Found wormhole vuln in %s : %s" % (ip, dumps(ret)))
                result.append((port, dumps(ret)))
        else:
            for p in port:
                res = poc_module.verify(ip, p)

def scan(target, threads):
    logger.info("Going to scan %s IPs" % len(target))
    pool = Pool(threads)
    _ = list(pool.imap_unordered(singleIpScanner, target))
    logger.info("Scanning Done.\n%d Possible")


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip",
                        help = "target ip to scan")
    parser.add_option("-f", "--file", dest="filename",
                        help="target IPs to scan(will ignore -i option)")
    parser.add_option("-v","--verbose", action="store_true", dest="verbose",
                        help="get more verbose output")
    parser.add_option("-V","--Verbose", action="store_true", dest="verbose",
                        help="get more verbose output")
    parser.add_option("-o", "--output", dest="output",
                        help="output file")
    parser.add_option("-t", "--threads", dest="threads",
                        help="threads number used for scan")
    (opt, args) = parser.parse_args()

    if not opt.filename and not opt.ip:
        parser.print_help()
        exit(1)

    if opt.verbose:
        logger.setLevel(logging.INFO)
    if opt.Verbose:
        logger.setLevel(logging.DEBUG)

    logger.name = "wormHoleScanner"
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
