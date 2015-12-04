#!/usr/bin/env python


protocol = ["http"]
port = [6259, 40310, 6677, ]


def verify(ip, port):
    try:
        resp = requests.post('http://%s:%d/getcuid' % (ip, port),
                data={"mcmdf":"inapp_", "callback":None},
                headers={"remote-addr":"127.0.0.1", "referer": "http://www.baidu.com"},
                timeout=0.5)

        if resp.status_code==200 or resp.status_code==403 or resp.status_code==500:
            #logger.debug("On port [%d] %s" %( port, resp.text))
            return resp.text
            # service_name = service[3:]
            # result[service_name] = json.loads(resp.text)
            # result[service_name]['port'] = port

    except requests.RequestException:
        continue
