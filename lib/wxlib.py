__author__ = 'hawk'
import json
import time
import netlib
import util
import re
import requests
import os
import configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cf = configparser.ConfigParser()
cf.read('.env')
if cf.get('property','env') == 'development':
    cf.read('config_dev.ini')
else:
    cf.read('config_prod.ini')

WEIXIN_GET_ACCESS_TOKEN =  cf.get('property','WEIXIN_GET_ACCESS_TOKEN')
WEIXIN_API_TOKEN =  cf.get('property','WEIXIN_API_TOKEN')
FFMPEG_EXECUTOR =  cf.get('property','FFMPEG_EXECUTOR')
TEMP_DIR =  cf.get('property','TEMP_DIR')
OSS_Domain =  cf.get('property','OSS_Domain')
OSS_Folder =  cf.get('property','OSS_Folder')


def getAccessToken(storeId):
    # return 'access_token:{}'.format(storeId)
    global WEIXIN_GET_ACCESS_TOKEN,WEIXIN_API_TOKEN
    timestamp = int(time.time())
    str = '{}-{:d}-ccwk7$'.format(WEIXIN_API_TOKEN,timestamp)
    signature = util.md5(str)
    url = '{}&store_id={}&timestamp={:d}&signature={}'.format(WEIXIN_GET_ACCESS_TOKEN,storeId,timestamp,signature)

    #test code
    # if storeId == 10008:
    if cf.get('property','env') == 'development':
        url = 'http://weixin.checheweike.com/get_access_token2.php?store_id=10034&token=1q2w3e4r5t6y7u8i9o0p1q2w3e4r5t6y7u8i9o0p'

    # print(url)
    result_obj = netlib.httpGet(url,'json')
    if 'status' in result_obj and result_obj['status'] == 1:
        return result_obj['access_token']
    else:
        return None

def getWxUser(storeId,openid):
    print('getWxUser')
    access_token = getAccessToken(storeId)
    print(access_token)
    if access_token == None:
        return None

    url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}&lang=zh_CN'.format(access_token,openid)
    try:
        result_obj = netlib.httpGet(url,'json')
        if result_obj != None and 'nickname' in result_obj:
            return result_obj
    except Exception as e:
            print('wxlib:get wx_user exception:{}'.format(e))

    return None


def sendTextMessage(storeId,openid,text):
    print('sendTextMessage')
    access_token = getAccessToken(storeId)
    print(access_token)
    if access_token == None:
        return None

    url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(access_token)
    message = {
        "touser":openid,
        "msgtype":"text",
        "text":
        {
            "content":text
        }
    }

    try:
        result_obj = netlib.httpPostRaw(url,message,'json')
    except Exception as e:
        print(e)
        return  None
    return result_obj


def sendPlainMessage(storeId,message):
    print('sendTemplateMessage')
    access_token = getAccessToken(storeId)
    print(access_token)
    if access_token == None:
        return None

    url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(access_token)
    try:
        result_obj = netlib.httpPostRaw(url,message['data'],'json')
    except Exception as e:
        print(e)
        return  None
    return result_obj


def sendTemplateMessage(storeId,message):
    print('sendTemplateMessage')
    access_token = getAccessToken(storeId)
    print(access_token)
    if access_token == None:
        return None

    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    try:
        result_obj = netlib.httpPostRaw(url,message['data'],'json')
    except Exception as e:
        print(e)
        return  None
    return result_obj

def sendGroupeMessage(storeId,message):
    print('sendGroupeMessage')
    access_token = getAccessToken(storeId)
    print(access_token)
    if access_token == None:
        return None

    if message['data'].get('filter'):
        url = 'https://api.weixin.qq.com/cgi-bin/message/mass/sendall?access_token={}'.format(access_token)
    else:
        url = 'https://api.weixin.qq.com/cgi-bin/message/mass/send?access_token={}'.format(access_token)

    try:
        result_obj = netlib.httpPostRaw(url,message['data'],'json')
    except Exception as e:
        print(e)
        return  None
    return result_obj


def fileTranser(ossBucket,storeId,mediaId):
    print('filetransfer')

    access_token = getAccessToken(storeId)
    if access_token == None:
        return None

    media_url = 'http://file.api.weixin.qq.com/cgi-bin/media/get?access_token={}&media_id={}'.format(access_token,mediaId)
    print(media_url)
    wxfile_response = requests.get(media_url)
    wxfile_path = mediaId

    reponse_headerinfo  = wxfile_response.headers
    file_type = reponse_headerinfo['Content-Type']
    print(reponse_headerinfo)
    #like  'Content-disposition': 'attachment; filename="cpSKeX_YbzYnRnu2ZBkwuj6FsiOpi_IW18dbnRuo61sUdF_BfZansehmdrK6LvHH.jpg"'
    if 'Content-disposition' in reponse_headerinfo:
        content_disposition = reponse_headerinfo['Content-disposition']
        m = re.findall(r'filename=\"(.+)\"', content_disposition)
        if len(m) > 0:
            wxfile_path = m[0]

    wxfile_name = wxfile_path
    #download file and save
    # file_dir = '/tmp/wx_temp_files/'
    #test
    file_dir = TEMP_DIR

    wxfile_path = file_dir + wxfile_path
    output = open(wxfile_path,'wb')
    output.write(wxfile_response.content)
    output.close()

    media_length = 0

    if wxfile_path.endswith('amr'): #audio
        mp3_path = wxfile_path[0:-4] + '.mp3'
        if os.path.isfile(mp3_path):
            os.remove(mp3_path)

        convert_shell_cmd = '{} -i {} {} 2>&1 | grep Duration'.format(FFMPEG_EXECUTOR,wxfile_path,mp3_path)
        result_str =  util.shellWithResult(convert_shell_cmd)
        print(type(result_str))
        print(result_str)
        if len(result_str) < 1:
            return None

        m = re.findall(r'Duration\:\s(\d{2}):(\d{2}):(\d{2}\.\d{2,})', result_str.decode('utf8'))
        if len(m) > 0 and len(m[0]) > 0:
            hh = int(m[0][0])
            mm = int(m[0][1])
            ss = float(m[0][2])
            media_length = int(hh*3600 + mm*60 + ss)

        if os.path.isfile(mp3_path):
            wxfile_path = mp3_path
            file_type= 'audio/mpeg'
        else:
            return None

    file_key = '{}/{}'.format(OSS_Folder,wxfile_name)
    print('file type:{0}'.format(file_type))
    res = ossBucket.put_object_from_file(file_key, wxfile_path)
    if (res.status / 100) == 2:
        return {
                'url' : OSS_Domain + file_key,
                'duration' : media_length
                }
    else:
        print('transfer failed: {}'.format(res.status))
        return None
