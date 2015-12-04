#!/usr/bin/env python

from utils.log import logger
from utils.concurrent import multiThread
import IPy
import itertools

def IP_Generator(ip_str_set):
    return list(itertools.chain.from_iterable(IPy.IP(ip_str, make_net=True)
                            for ip_str in ip_str_set))
