import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.Html_Downloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		#启动爬虫循环
		while self.urls.has_new_url():  
			try: 
				#取出待爬取url
				new_url = self.urls.get_new_url()  
				print ('craw %d : %s' % (count,new_url))
				#启动下载器下载页面
				html_cont = self.downloader.download(new_url)
				#调用解析器解析，得到新的url列表以及新的数据  
				new_urls, new_data = self.parser.parse(new_url, html_cont) 
				#将新的url补充进url管理器    
				self.urls.add_new_urls(new_urls) 
				#收集数据              
				self.outputer.collect_data(new_data)           

				if count == 10:
					break
				count = count + 1
			except Exception as e:
				print(str(e))
		self.outputer.output_html()

if __name__=="__main__":
	root_url = "http://baike.baidu.com/item/Python"
	obj_spider = SpiderMain()
	#启动爬虫
	obj_spider.craw(root_url)  