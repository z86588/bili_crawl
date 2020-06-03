# -*- coding: utf-8 -*-
import scrapy
import json
from bili_crawl.content_list import ContentList


class BiliUgcSpiderSpider(scrapy.Spider):
    name = 'bili_ugc_spider'

    allowed_domains = ['api.bilibili.com']
    cl = ContentList()
    # start_urls = ['https://api.bilibili.com/']
    start_urls = cl.ugc_uri

    def parse(self, response):
        pass
