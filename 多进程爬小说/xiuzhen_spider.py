'''
import requests,re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from multiprocessing import Pool



def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    bsobj = BeautifulSoup(r.text,'lxml')
    return bsobj
#/ddk6728/4216600.html
def get_url(url):
    soup = get_html(url)
    urls = set()
    for link in soup.find_all('a',href=re.compile('^/ddk1597/\d+\.html$')):
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
    data['content'] = article_content.get_text('\r\n    ',strip=True)
    return data

def write_book(url):
        all_url = get_url(url)
        pool = Pool(10)
        pool.map(main,[x for x in all_url])

def main(x):
    with open('book.txt','w',encoding='utf-8') as b: 
        data = get_data(x)
        title = data['title']
        delete6 = '以下是为你提供的《》小说（正文）正文，敬请欣赏！'
        b.write(title)
        b.write('\r\n    ')
        content = data['content'].lstrip().lstrip(delete6)
        b.write(content)
        b.write('\r\n')
        print(title)


if __name__ == '__main__':
    url = 'http://www.dingdiann.com/ddk1597/'
    write_book(url)
    # pool = Pool()
    # pool.map()
'''


import requests,re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    bsobj = BeautifulSoup(r.text,'lxml')
    return bsobj
#/ddk6728/4216600.html
def get_url(url):
    soup = get_html(url)
    urls = set()
    for link in soup.find_all('a',href=re.compile('^/ddk1597/\d+\.html$')):
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
    data['content'] = article_content.get_text('\r\n    ',strip=True)
    return data

def write_book(url):
    with open('book.txt','w',encoding='utf-8') as b:
        n = 0
        delete1 = 'chaptererror();'
        delete2 = '最新全本：、、、、、、、、、、'
        delete3 = '欢迎广大书友光临阅读，最新、最快、最全的全本小说尽在！&amp;lt;/a&amp;gt;'
        delete4 = 'target=”_blank”></a>"target="_blank"></a></a></a>'
        delete5 = '&amp;lt;ahref=;gt;target=”_bla="_blank">”</a></a>target=”_bla="_blank"></a>”</a>'
        delete6 = '以下是为你提供的《》小说（正文）正文，敬请欣赏！'
        all_url = get_url(url)
        for x in all_url:
            n += 1
            data = get_data(x)
            title = data['title']
            b.write(title)
            b.write('\r\n    ')
            content = data['content'].lstrip().lstrip(delete6).rstrip(delete1).rstrip().rstrip(delete2).rstrip().rstrip(delete3).rstrip().rstrip(delete4).rstrip().rstrip(delete5)
            b.write(content)
            b.write('\r\n')
            print('第{}章爬取完成'.format(n))

if __name__ == '__main__':
    url = 'http://www.dingdiann.com/ddk1597/'
    write_book(url)