# -*- coding: utf-8 -*-
import scrapy


class BiliPgcSpiderSpider(scrapy.Spider):
    name = 'bili_pgc_spider'
    allowed_domains = ['api.bilibili.com']
    start_urls = ['http://api.bilibili.com/']

    def parse(self, response):
        pass
