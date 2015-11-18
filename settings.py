#!/usr/bin/env python
# coding=utf-8

#----------------logger---------------------
import logging
from exp.pocFor360 import pocFor360
#import tempfile

logger = logging.getLogger("wormHoleScanner")

logger.setLevel(logging.WARN)


#fh = logging.FileHandler('/tmp/wormhole.log')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#fh.setFormatter(formatter)
ch.setFormatter(formatter)
#logger.addHandler(fh)
logger.addHandler(ch)
#----------------logger---------------------



#----------------ports-----------------------
#target_ports = [6259, 40310, 7777, 8766, 6677]
# moplus 40310 6259
# frontia 7777
# 高德地图 6677
# 新浪 9527
# 360 38516
#----------------ports-----------------------
#----------------info------------------------
#target_infos = ["geolocation", "getcuid"]
#----------------info------------------------

#---------------Target------------------------
target = {
        "geolocation" : [6259, 40310, 6677, ],
        "getcuid" : [6259, 40310, ],
        "360_POC" : {
                        'port' : 38517,
                        'exp' : pocFor360
                    }
        }

#---------------Target------------------------



#----------------Thread------------------------
THREAD_NUMBER = 50

#----------------Thread------------------------
