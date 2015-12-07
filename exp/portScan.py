#!/usr/bin/env python

import socket
from utility import logger
socket.setdefaulttimeout(1.0)
port = [7777, 6587, 55279]

def verify(ip, port):
    try:
        # logger.info("scanning %s:%d"% (ip, port))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print "%s:%d" % (ip, port)
        # if ip=="10.221.139.247" and port==7777:
        #     logger.warn("-----------------10.221.139.247:7777")
        s.connect((ip, port))
        s.close()
        # if ip=="10.221.139.247" and port==7777:
        #      logger.warn("-----------------10.221.139.247:7777 is open")
        return "open"
    except Exception,e:
        # logger.error(e)
        # if ip=="10.221.139.247" and port==7777:
        #     logger.warn("-----------------10.221.139.247:7777 is close")
        return None
