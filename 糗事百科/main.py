import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.qiushibaike.com/'

def get_html(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		'Accept':'text/css,*/*;q=0.1'
	}
	r = requests.get(url,headers=headers)
	r.encoding = 'utf8'
	bsobj = BeautifulSoup(r.text,'lxml')
	return bsobj

def get_picture(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		'Accept':'text/css,*/*;q=0.1'
	}
	r = requests.get(url,headers=headers)
	return r.content

def get_jokes(url):
	'''
	获取糗事百科段子
	:param url: 
	:return: 
	'''
	joke_list = []
	soup = get_html(url)
	jokes = soup.find_all('div',class_='article block untagged mb15 typs_hot')
	i = 0
	for joke in jokes:
		article = joke.find('div',class_='content').get_text(strip=True)
		author = joke.find('img')['alt']
		if joke.find('div',class_='thumb'):
			url = joke.find('div',class_='thumb').img['src']
			pic_url = 'http:'+url
			pic = get_picture(pic_url)
			print('作者：{}\n{}\n搞笑图{} {}\n'.format(author,article,i,pic_url))
			with open('搞笑图{}.jpg'.format(str(i)),'wb') as p:
				p.write(pic)
			i+=1
		else:
			print('作者：{}\n{}\n'.format(author,article))
		


if __name__ == '__main__':
	get_jokes(url)
