__author__ = 'hawk'
import json
import requests

def httpPost(url,values,type='text'):
    response = requests.post(url, data=values,verify=False)
    if type == 'json':
        return response.json()
    else:
        return response.text

def httpPostRaw(url,values,type='text'):
    response = requests.post(url, data=json.dumps(values,ensure_ascii=False).encode('utf8'),verify=False)
    if type == 'json':
        return response.json()
    else:
        return response.text

def httpGet(url,type='text'):
    r = requests.get(url)
    if type == 'json':
        return r.json()
    else:
        return r.text

