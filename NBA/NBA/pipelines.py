# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class NbaPipeline:
    def __init__(self):
        self.conn = MongoClient()
        self.db = self.conn.PTT
        self.collection = self.db.NBA

    def process_item(self, item, spider):
        try:
            self.collection.insert_one(dict(item))
        except:
            pass
        return item
