# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MongoPipeline(object):
    collection_name = 'users'

    def __init__(self,mongo_uri,mongo_db,mongo_user,mongo_pwd):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_user = mongo_user
        self.mongo_pwd = mongo_pwd
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.client.admin.authenticate(mongo_user, mongo_pwd)

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_user=crawler.settings.get('MONGO_USER'),
            mongo_pwd=crawler.settings.get('MONGO_PWD')
        )

    def open_spider(self,spider):
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].update({'url_token':item['url_token']},{'$set':dict(item)},True)
        return item
