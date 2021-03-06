#!/usr/bin/env python

import requests
#from settings import logger
import settings
import urllib
import urllib2
import socket
import httplib

def pocForGaode(ip):
    try:
        #settings.logger.info("test")
        target_url = "http://%s:6677/geolocation?"  % ip
    #    resp = requests.get(target_url, headers={"referer":"http://114.247.50.32"},timeout=0.5)
        req = urllib2.Request(target_url)
        req.add_header("referer", "http://114.247.50.32")
        resp = urllib2.urlopen(req, timeout=2.0)
        #settings.logger.info(resp)
        status_code = resp.getcode()
        if status_code in [200, 403, 500]:
            return {"result":resp.read()}
        else:
            return None

    except Exception:
        return None
#    except urllib2.HTTPError, e:
#        settings.logger.debug(e)
#        return None
#    except socket.timeout,e:
#        settings.logger.debug(e)
#        return None
#    except urllib2.URLError, e:
#        settings.logger.debug(e)
#        return None


if __name__=="__main__":
    import sys
    print pocForGaode(sys.argv[1])
