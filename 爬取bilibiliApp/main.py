import requests
from pprint import pprint



if __name__ == '__main__':
    url = ('https://app.bilibili.com/x/v2/rank?'
        'appkey=1d8b6e7d45233436&'
        'build=514000&'
        'mobi_app=android&'
        'order=all&'
        'platform=android&'
        'pn=1&ps=60&ts=1506603326&'
        'sign=98cef67e41bdd61ae047794be8649bd6')
    headers = {
        'Display-ID': '1281250-1506602849',
        'Buvid':'51A47D40-A516-47F5-BC93-895AFA77429129452infoc',
        'User-Agent': 'Mozilla/5.0 BiliDroid/5.14.0 (bbcallen@gmail.com)',
        'Device-ID': 'GSFDIBFwQ3cVcBMlWSVHdhVxRXxILW0MawVhUiBcZFEkRSdKfR8sWWsM',
        'Host': 'app.bilibili.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Cookie': 'sid=8o1zw4ar',
        }
    r = requests.get(url = url,headers = headers,verify = False)
    r.encoding = 'utf8'
    data = r.json()['data']
    L = []
    for d in data:
        L.append(d['title'])

    pprint(L)
