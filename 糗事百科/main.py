import re,requests,random
from bs4 import BeautifulSoup

url = 'https://www.qiushibaike.com/'
path = '搞笑图{}.jpg'

class QiuBai():
	def __init__(self,url,path):
		self.url = url
		self.path = path
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
			'Accept': 'text/css,*/*;q=0.1'
		}
		self.joke_list = []

	def __get_html(self):
		r = requests.get(self.url, headers=self.headers)
		r.encoding = 'utf8'
		bsobj = BeautifulSoup(r.text, 'lxml')
		return bsobj


	def __get_picture(self,url):
		r = requests.get(url, headers=self.headers)
		return r.content


	def __get_joke_list(self):
		'''
		获取糗事百科段子
		:return: 
		'''
		soup = self.__get_html()
		jokes = soup.find_all('div', class_='article block untagged mb15 typs_hot')
		i = 0
		for joke in jokes:
			article = joke.find('div', class_='content').get_text(strip=True)
			author = joke.find('img')['alt']
			if joke.find('div', class_='thumb'):
				url = joke.find('div', class_='thumb').img['src']
				pic_url = 'http:' + url
				pic = self.__get_picture(pic_url)
				with open(self.path.format(str(i)), 'wb') as p:
					p.write(pic)
				article = '作者：{}\n{}\n'.format(author, article)
				self.joke_list.append(article)
				i += 1
			else:
				article = '作者：{}\n{}\n'.format(author, article)
				self.joke_list.append(article)
		

	def get_joke(self):
		self.__get_joke_list()
		new_joke = random.choice(self.joke_list)
		return new_joke

if __name__ == '__main__':
	j = QiuBai(url,path)
	joke = j.get_joke()
	print(joke)
