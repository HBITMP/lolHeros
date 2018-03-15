# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import hashlib
import pymongo
import requests
import re
import os

class LolspiderPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    def process_item(self, item, spider):
        self.db['LOL'].insert(dict(item))
        for i,img in enumerate(item['wallpaper']):
            filepath = "{os}\img\{name}\{item}.jpg".format(os=os.getcwd(), name=item['heros_name'], item=item['imgname'][i])
            dir = "{os}\img\{name}".format(os=os.getcwd(), name=item['heros_name'])
            if not os.path.exists(dir):
                os.makedirs(dir)
            result = re.match('(http://ossweb-img.qq.com/images/lol/web201310/skin/).*?(\d+\S+)', img)
            string = result.group(1) + 'big' + result.group(2)
            response = requests.get(string)
            with open(filepath, 'wb') as f:
                f.write(response.content)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
