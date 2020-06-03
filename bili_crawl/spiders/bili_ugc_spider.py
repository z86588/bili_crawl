# -*- coding: utf-8 -*-
import scrapy
import json
from bili_crawl.items import UgcItem


class BiliUgcSpiderSpider(scrapy.Spider):
    name = 'bili_ugc'

    allowed_domains = ['api.bilibili.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/ranking?rid=0&day=3&type=1&arc_type=0&jsonp=jsonp']

    # start_urls = cl.ugc_uri

    def parse(self, response):
        body = response.body.decode('utf8')
        c_list = json.loads(body)['data']['list']

        for c in c_list:
            item = UgcItem()
            item['ugc_aid'] = c.get('aid')
            item['ugc_title'] = c.get('title')
            print(item['ugc_title'])
