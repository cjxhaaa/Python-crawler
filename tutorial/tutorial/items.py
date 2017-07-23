# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CmozItem(scrapy.Item):
	#网站名字
	title = scrapy.Field()
	#url
	link = scrapy.Field()
	#网站描述
	desc = scrapy.Field()


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
