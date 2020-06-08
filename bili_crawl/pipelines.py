# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi


# from bili_crawl import settings


class BiliCrawlPipeline:
    def process_item(self, item, spider):
        return item


class BiliUgcPipeline:
    ugc_table = 'bili_ugc_crawl'

    def __init__(self, dbpool):
        self.item_list = []
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PW'],
            charset='UTF8mb4',
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )

        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        self.item_list.append(
            (item['ugc_aid'], item['ugc_bvid'], item['ugc_author'], item['ugc_coins'], item['ugc_duration'],
             item['ugc_mid'], item['ugc_image'], item['ugc_play'], item['ugc_pts'], item['ugc_title'],
             item['ugc_review'], item['ugc_rank'], item['ugc_area'], item['ugc_day'], item['ugc_type'],
             item['ugc_type_r'], item['ugc_crawl_time']))
        if len(self.item_list) == 500:
            bulk_item = self.item_list[:]
            query = self.dbpool.runInteraction(self.do_bulk_insert, bulk_item)
            query.addErrback(self.handle_error)
            self.item_list.clear()
        return item

    # def do_insert(self, cursor, item):
    #     """
    #     单条插入
    #     :param cursor:
    #     :param item:
    #     """
    #     insertSql = """
    #     insert into bili_ugc_rank (ugc_aid, ugc_bvid, ugc_author, ugc_coins, ugc_duration, ugc_mid, ugc_image,
    #     ugc_play, ugc_pts, ugc_title, ugc_review, ugc_rank, ugc_area, ugc_day, ugc_type, ugc_type_r, ugc_crawl_time)
    #     values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    #     """
    #     cursor.execute(insertSql, (
    #         item['ugc_aid'], item['ugc_bvid'], item['ugc_author'], item['ugc_coins'], item['ugc_duration'],
    #         item['ugc_mid'], item['ugc_image'], item['ugc_play'], item['ugc_pts'], item['ugc_title'],
    #         item['ugc_review'], item['ugc_rank'], item['ugc_area'], item['ugc_day'], item['ugc_type'],
    #         item['ugc_type_r'], item['ugc_crawl_time']))

    def do_bulk_insert(self, cursor, item_list):
        # print('>>>>enter bulk insert!')
        insertSql = """
        insert into bili_ugc_rank (ugc_aid, ugc_bvid, ugc_author, ugc_coins, ugc_duration, ugc_mid, ugc_image, 
        ugc_play, ugc_pts, ugc_title, ugc_review, ugc_rank, ugc_area, ugc_day, ugc_type, ugc_type_r, ugc_crawl_time) 
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(insertSql, item_list)

    def handle_error(self, exception):
        print('Error: ', exception)

    def close_spider(self, spider):
        print("closing spider,last commit", len(self.item_list))
        query = self.dbpool.runInteraction(self.do_bulk_insert, self.item_list)
        query.addErrback(self.handle_error)
