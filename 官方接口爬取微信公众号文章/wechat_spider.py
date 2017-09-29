import requests
import json
import re
import random

text = '国庆'
APP_ID = 'wx68c7f70e73029e26'
APP_SERCRET = 'd0eb6851932ae501fe94a6c1160c4e18'
url = 'https://mp.weixin.qq.com/'
with open('cookies.txt','r') as f:
    cookies = json.load(f)

def get_token():
    response = requests.get(url,cookies=cookies)
    # token = re.search(r'token=\d+',response.url).group()
    # print(token)
    token = re.findall(r'token=(\d+)',response.url)[0]
    return token

def get_data():
    new_url = 'https://mp.weixin.qq.com/cgi-bin/operate_appmsg?sub=check_appmsg_copyright_stat'
    params = {
        'token':str(get_token()),
        'lang':'zh_CN',
        'ajax':'1',
        'random':str(random.random()),
        'url':text,
        'begin':'0',
        'count':'3'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36X-Requested-With:XMLHttpRequest',
        'Referer':'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&share=1&type=10&lang=zh_CN&token=300257709',
        'Host':'mp.weixin.qq.com'
    }
    response = requests.post(new_url,headers=headers,cookies=cookies,params=params)
    L = response.json()['list']
    n = 0
    for l in L:
        n+=1
        print('第{}篇文章'.format(n))
        print('标题：{}'.format(l['title']))
        print('作者：{}'.format(l['nickname']))
        print('文章地址：{}'.format(l['url']))





if __name__ == '__main__':
    get_data()

# class Basic():
#     def __init__(self,appId,appSecret):
#         self.appId = appId
#         self.appSecret = appSecret
#
#     def get_access_token(self):
#         payload_access_token={
#             'grant_type':'client_credential',
#             'appid':self.appId,
#             'secret':self.appSecret
#         }
#         postUrl = 'https://api.weixin.qq.com/cgi-bin/token'
#         r = requests.get(postUrl,params=payload_access_token)
#         dict_result = r.json()
#         return dict_result['access_token']
#
# if __name__ == '__main__':
#     b = Basic(APP_ID,APP_SERCRET)
#     print(b.get_access_token())