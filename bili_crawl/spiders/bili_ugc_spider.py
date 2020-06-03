# -*- coding: utf-8 -*-
import scrapy
import json

class BiliUgcSpiderSpider(scrapy.Spider):
    name = 'bili_ugc'

    allowed_domains = ['api.bilibili.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/ranking?rid=0&day=3&type=1&arc_type=0&jsonp=jsonp']
    # start_urls = cl.ugc_uri

    def parse(self, response):
        body = response.body.decode('utf8')
        c_list = json.loads(body)['data']['list']
        print(c_list[0])
