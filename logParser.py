#!/usr/bin/env python
# coding=utf-8
import json
import sys
import csv
from collections import defaultdict
from pprint import pprint

import time


# writer.writerow(["ip","cuid","cuid_port" ,"citycode", "latitude", "longtitude", "accuracy", "location_port","360_result", "360_port"])

def tryGet(d, k):
    if not d :return ""
    return d[k] if k in d else ""

input_file = sys.stdin
if len(sys.argv)>=2:
    input_file = open(sys.argv[1], "r")

logInfo = defaultdict(list)
ports = set()

for line in input_file:
    if not line.strip():
        continue

    index = line.index("in")

    info = line[index+2:]

    # split ip
    index = info.index(":")
    ip = info[:index].strip()

    # split port
    info = info[index+1:]
    index = info.index(':')
    port = info[:index].strip()

    ports |= (set([port]))

    # split result
    result = info[index+1:].strip()

    logInfo[ip].append((port, result))

    #break


Fields = ["ip"] + list(ports)
writer =csv.DictWriter(open("wormhole_log_%s.csv" % time.strftime("%Y-%m-%d",time.localtime(time.time())), "wb"), fieldnames=Fields)
writer.writerow(dict(zip(Fields, Fields)))

#pprint(dict(logInfo))
for ip in logInfo:
    row = {
            "ip":ip,
        }
    for t in logInfo[ip]:
        row[t[0]] = t[1]
    writer.writerow(row)
