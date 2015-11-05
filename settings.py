#!/usr/bin/env python 

#----------------logger---------------------
import logging

logger = logging.getLogger("wormHoleScanner")

logger.setLevel(logging.WARN)


fh = logging.FileHandler('/tmp/wormhole.log')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
logger.addHandler(fh)
logger.addHandler(ch)
#----------------logger---------------------



#----------------ports-----------------------

target_ports = [6259, 40310, 7777, 8766, 6677]

#----------------ports-----------------------


#----------------info------------------------

target_infos = ["geolocation", "getcuid"]

#----------------info------------------------


#----------------Thread------------------------
THREAD_NUMBER = 50

#----------------Thread------------------------



