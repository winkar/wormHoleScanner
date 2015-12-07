#!/usr/bin/env python

import IPy
import itertools
import logging

logger = logging.getLogger("wormHoleScanner")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

logger.addHandler(streamHandler)


def IP_Generator(ip_str_set):
    return list(map(str, itertools.chain.from_iterable(IPy.IP(ip_str, make_net=True)
                            for ip_str in ip_str_set)))


def AttributeDict:

    def __init__(self):
        self.attr_dict = {}

    def __getattr__(self, key):
        if key in self.attr_dict:
            return self.attr_dict
        else:
            return None

    def __setattr__(self, key, value):
        self.attr_dict[key] = value


global_options = AttributeDict()
