# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from bili_crawl import settings

class BiliCrawlPipeline:
    def process_item(self, item, spider):
        return item


class BiliPgcPipeline:
    ugc_table = 'bili_ugc_crawl'

    def __init__(self, dbpool):
        self.dbpool = dbpool
