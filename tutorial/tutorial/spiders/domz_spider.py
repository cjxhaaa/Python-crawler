# 为了创建一个Spider，您必须继承 scrapy.Spider 类， 且定义以下三个属性:





import scrapy

class DmozSpider(scrapy.Spider):
	# name: 用于区别Spider,必须是唯一
	name = 'dmoz'
	#约束搜索的域名范围
	allowed_domains = ['dmoz.org']
	# start_urls: 包含了Spider在启动时进行爬取的url列表。 
	# 因此，第一个被获取到的页面将是其中之一。 
	# 后续的URL则从初始的URL获取到的数据中提取。
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]
	# parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 
	# 该方法负责解析返回的数据(response data)，提取数据(生成item)以及
	# 生成需要进一步处理的URL的 Request 对象。
	def parse(self,response):
		# Response 对象将会作为唯一的参数传递给该函数。 
		# filename = response.url.split('/')[-2]
		# with open(filename,'wb') as f:
		# 	f.write(response.body)
		for sel in response.xpath('//ul/li'):
			title = sel.xpath('a/text()').extract()
			link = sel.xpath('a/@href').extract()
			desc = sel.xpath('text()').extract()