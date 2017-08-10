import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
#verify 禁止证书验证
response = requests.get(url,verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
for x in stations:
	print(x)
print(dict(stations).keys())
print(dict(stations).values())