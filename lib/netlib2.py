__author__ = 'hawk'
import json
import urllib2

def httpPost(url, values, type='text'):
    try:
        data_str = json.dumps(values)
        req = urllib2.Request(url, data_str)
        response = urllib2.urlopen(req)
        resp_body = response.read()
        if resp_body == None or len(resp_body) == 0:
            return None

        if type == 'json':
            json_obj = json.loads(resp_body)
            return json_obj
        else:
            return resp_body
    except Exception, e:
        print 'http_post error', e
        return None

def httpGet(url, type='text'):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)

        resp_body = response.read()
        if resp_body == None or len(resp_body) == 0:
            return None

        if type == 'json':
            json_obj = json.loads(resp_body)
            return json_obj
        else:
            return resp_body
    except Exception, e:
        print 'http_get error', e
        return None

