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

global_options = None
