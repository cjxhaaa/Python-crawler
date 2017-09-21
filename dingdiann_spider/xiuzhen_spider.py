import requests,re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class DingDian():
    def __init__(self,url,bookname):
        self.url = url
        self.soup = self.get_html(self.url)
        self.bookname = bookname + '.txt'
        

    def get_html(self,url):
        r = requests.get(url)
        r.encoding = 'utf8'
        bsobj = BeautifulSoup(r.text,'lxml')
        return bsobj
    #/ddk6728/4216600.html
    def get_url(self):
      
        urls = set()
        for link in self.soup.find_all('a',href=re.compile('^/ddk\d+/\d+\.html$')):
            if 'href' in link.attrs:
                new_url = urljoin(self.url,link['href'])
                urls.add(new_url)
        new_urls = sorted(list(urls))
        return new_urls

    def get_data(self,url):
        soup = self.get_html(url)
        data = dict()
        article_title = soup.find('div',class_='bookname').find('h1')
        if article_title is None:
            data['title'] = '无标题'
        data['title'] = article_title.get_text() 
        article_content = soup.find('div',id='content')
        if article_content is None:
            data['content'] = '无正文'
        data['content'] = article_content.get_text('\r\n    ',strip=True)
        return data

    def write_book(self):
        with open(self.bookname,'w',encoding='utf-8') as b:
            n = 0
            delete1 = 'chaptererror();'
            delete2 = '最新全本：、、、、、、、、、、'
            delete3 = '欢迎广大书友光临阅读，最新、最快、最全的全本小说尽在！&amp;lt;/a&amp;gt;'
            delete4 = 'target=”_blank”></a>"target="_blank"></a></a></a>'
            delete5 = '&amp;lt;ahref=;gt;target=”_bla="_blank">”</a></a>target=”_bla="_blank"></a>”</a>'
            delete6 = '以下是为你提供的《》小说（正文）正文，敬请欣赏！'
            all_url = self.get_url()
            for x in all_url:
                n += 1
                data = self.get_data(x)
                title = data['title']
                b.write(title)
                b.write('\r\n    ')
                content = data['content'].lstrip().lstrip(delete6).rstrip(delete1).rstrip().rstrip(delete2).rstrip().rstrip(delete3).rstrip().rstrip(delete4).rstrip().rstrip(delete5)
                b.write(content)
                b.write('\r\n')
                print('第{}章爬取完成'.format(n))

if __name__ == '__main__':
    # url = input('爬取小说url：')
    # bookname = input('小说名字：')
    url = 'http://www.dingdiann.com/ddk6728/'
    bookname = '123'
    D = DingDian(url,bookname)
    D.write_book()