#!/usr/bin/env python
import json
import sys
import csv
from functools import partial

import time

writer =csv.writer(open("wormhole_log_%s.csv" % time.strftime("%Y-%m-%d",time.localtime(time.time())), "wb"))

writer.writerow(["ip","cuid","cuid_port" ,"citycode", "latitude", "longtitude", "accuracy", "location_port"])

def tryGet(d, k):
    if not d :return ""
    return d[k] if k in d else ""

for line in sys.stdin:
    index = line.index("in")
    info = line[index+2:]
    index = info.index(":")
    ip = info[:index].strip()
    other_info = json.loads(info[index+1:].strip())
    location = other_info['location'] if 'location' in other_info else {}
    cuid = other_info['cuid'] if 'cuid' in other_info else {}

    tryGetl = partial(tryGet, location) 
    tryGet2 = partial(tryGet, tryGetl(u"coords"))
    writer.writerow( [ip, tryGet(cuid, 'cuid'), tryGet(cuid,"port"), tryGetl(u'citycode'), tryGet2(u"latitude"), tryGet2(u"longitude"), tryGet2(u"accuracy"), tryGetl("port")])

        

