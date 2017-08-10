import requests,re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


url = 'http://www.dingdiann.com/ddk6728/'
def get_html(url):
	r = requests.get(url)
	r.encoding = 'utf8'
	bsobj = BeautifulSoup(r.text,'lxml')
	return bsobj
#/ddk6728/4216600.html
def get_url(url):
	soup = get_html(url)
	urls = set()
	for link in soup.find_all('a',href=re.compile('^/ddk6728/\d+\.html$')):
		if 'href' in link.attrs:
			new_url = urljoin(url,link['href'])
			urls.add(new_url)
	new_urls = sorted(list(urls))
	return new_urls

def get_data(url):
	soup = get_html(url)
	data = dict()
	article_title = soup.find('div',class_='bookname').find('h1')
	if article_title is None:
		datas['title'] = '无标题'
	data['title'] = article_title.get_text() 

	article_content = soup.find('div',id='content')
	if article_content is None:
		datas['content'] = '无正文'
	data['content'] = article_content.get_text()
	return data

def write_book(url):
	with open('book.txt','w',encoding='utf-8') as b:
		n = 0
		for x in get_url(url):
			n += 1
			data = get_data(x)
			title = data['title']
			b.write(title)
			content = data['content']
			b.write(content)
			print('第{}章爬取完成'.format(n))


if __name__ == '__main__':
	write_book(url)
