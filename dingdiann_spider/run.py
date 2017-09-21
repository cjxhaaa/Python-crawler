from xiuzhen_spider import DingDian

if __name__ == '__main__':
    url = input('爬取小说url：')
    bookname = input('小说名字：')
    D = DingDian(str(url),str(bookname))
    D.write_book()

# if __name__ == '__main__':

#     url = 'http://www.dingdiann.com/ddk6728/'
#     bookname = '123'
#     D = DingDian(url,bookname)
#     D.write_book()