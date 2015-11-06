#!/usr/bin/env python
# coding=utf-8

#from gevent.pool import Pool
#from multiprocessing.dummy import Pool
from pool import ScannerPool
from IPy import IP
from wormHolePoc import  checkIP
from settings import THREAD_NUMBER
from settings import logger

from json import dumps


def getAllIp(ip):
    for ip in IP(ip, make_net=True):
        yield str(ip)



def singleIpScanner(ip):
    logger.info("Start to scan %s" % ip)
    ret = checkIP(ip)
    if ret:
        logger.warn("Found wormhole vuln in %s : %s" % (ip, dumps(ret)))



def scan(ip):
    try:
        pool = ScannerPool.getPool()
        logger.info("Scanner to %s started" % ip)
        for _ in pool.imap_unordered(singleIpScanner, getAllIp(ip)):pass
        logger.info("Scan to %s done." % ip)
    except Exception,e:
        print e
        import traceback; traceback.print_exc()

if __name__=="__main__":
    try:
        import sys
        if len(sys.argv)<2:
            print "Usage: %s ip" % sys.argv[0]
            exit(1)
        scan(sys.argv[1])
    except KeyboardInterrupt:
        print "done"
        exit(2)
