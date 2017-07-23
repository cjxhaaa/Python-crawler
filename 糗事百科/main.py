import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def spider(url):
	r = requests.get(url)
	page = r.text
	soup = BeautifulSoup(page,'html.parser')
	texts = soup.find_all('div',class_='content')
	jokes = []
	x = 0
	for text in texts:
	    dt = text.get_text().strip('\n')
	    
	    x += 1
	    print(('第{}个笑话：{}').format(x,dt))
	    jokes.append(dt)

if __name__ == '__main__':
	url = 'https://www.qiushibaike.com/'
	spider(url)




