import requests
from bs4 import BeautifulSoup


url = 'https://www.zhihu.com/'
r = requests.get(url)
print(r.text)