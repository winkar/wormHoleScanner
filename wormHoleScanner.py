#!/usr/bin/env python
#coding=utf-8


from ipSegmentScanner import scan as ipSegmentScan
from optparse import OptionParser 
from settings import logger
import logging

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip",
                        help = "target ip to scan")
    parser.add_option("-f", "--file", dest="filename",
                        help="target IPs to scan")
    parser.add_option("-v","--verbose", action="store_true", dest="verbose",
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

    if opt.output:
        fh = logging.FileHandler(opt.output)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    
        
    if opt.filename:
        with open(opt.filename, "rb") as f:
            for line in f:
                if line.lstrip(" ").startswith("#"):
                    continue

                if opt.threads:
                    ipSegmentScan(line, opt.threads)
                else:
                    ipSegmentScan(line)
    if opt.ip:
        if opt.threads:
            ipSegmentScan(opt.ip, opt.threads)
        else:
            ipSegmentScan(opt.ip)



