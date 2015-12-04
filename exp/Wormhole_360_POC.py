#!/usr/bin/env python

import requests
#from settings import logger
#import settings

protocol = ["http"]
port = [38517]

def verify(domain):
    try:
        target_url = "http://%s:38517/getClientInfo"  % domain
        resp = requests.post(target_url, data ={"callback":"xxxx"},timeout=0.5)
        if resp.status_code==200 or resp.status_code==403 or resp.status_code==500:
            return resp.text
        else:
            return None
    except requests.RequestException,e:
        return None
