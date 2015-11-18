#!/usr/bin/env python
# coding=utf-8

import requests
#from settings import target_ports
from settings import target
import logging
from settings import logger
#from settings import target_infos
from optparse import OptionParser
import json


def checkIP(ip):
    result = {}
#    for port in  target_ports:
#        for service in target_infos:
    for service in target:
        if service in result:
            break

        if type(target[service]) is dict:
            #logger.info(service)
            retval = target[service]['exp'](ip)
            # if retval is None
            # means no result gotten
            # if empty {} means empty result but port is open
            if retval is None: continue
            result[service] = retval
            result[service]['port'] = target[service]['port']
            continue

        for port in target[service]:
            try:
                resp = requests.post('http://%s:%d/%s' % (ip, port, service),
                        data={"mcmdf":"inapp_", "callback":None},
                        headers={"remote-addr":"127.0.0.1", "referer": "http://www.baidu.com"},
                        timeout=0.5)

                if resp.status_code==200 or resp.status_code==403 or resp.status_code==500:
                #if "error" in resp.text:
                    #logger.warn("%d"%resp.status_code)
                    logger.debug("On port [%d] %s" %( port, resp.text))
                    service_name = service[3:]
                    result[service_name] = json.loads(resp.text)
                    result[service_name]['port'] = port
#                    result[service] = resp.text

            #except requests.exceptions.ConnectionError:
            #except requests.exceptions.ReadTimeout:
            except requests.RequestException:
                continue
    return result


if __name__=="__main__":
    parser = OptionParser()
    parser.add_option("-t", "--target", dest="ip",
                        help="target IP to scan")
    parser.add_option("-v","--verbose", action="store_true", dest="verbose",
                        help="get more verbose output")
    (opt, args) = parser.parse_args()

    if not opt.ip:
        parser.print_help()
        exit(1)

    if opt.verbose:
        logger.setLevel(logging.DEBUG)


    res= checkIP(opt.ip)
    from pprint import pprint
    pprint(res)
