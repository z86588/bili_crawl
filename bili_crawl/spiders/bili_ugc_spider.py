# -*- coding: utf-8 -*-
import scrapy
import json
import time
from bili_crawl.items import UgcItem
from content_list import ContentList
from urllib import parse


class BiliUgcSpiderSpider(scrapy.Spider):
    name = 'bili_ugc'

    url_list = ContentList().ugc_uri

    allowed_domains = ['api.bilibili.com']
    # start_urls = ['https://api.bilibili.com/x/web-interface/ranking?rid=0&day=3&type=1&arc_type=0&jsonp=jsonp']
    start_urls = url_list[:]

    def parse(self, response):
        body = response.body.decode('utf8')
        c_list = json.loads(body)['data']['list']
        params = parse.parse_qs(parse.urlparse(response.url).query)
        u_rid = params['rid'][0]
        u_day = params['day'][0]
        u_type = params['type'][0]
        u_type_r = params['arc_type'][0]
        u_date = time.strftime("%Y-%m-%d", time.localtime())

        for c in c_list:
            item = UgcItem()
            item['ugc_aid'] = c['aid']
            item['ugc_bvid'] = c['bvid']
            item['ugc_author'] = c['author']
            item['ugc_coins'] = c['coins']
            item['ugc_duration'] = c['duration']
            item['ugc_mid'] = c['mid']
            item['ugc_image'] = c['pic']
            item['ugc_play'] = c['play']
            item['ugc_pts'] = c['pts']
            item['ugc_title'] = c['title']
            item['ugc_review'] = c['video_review']
            item['ugc_rank'] = c_list.index(c)
            item['ugc_area'] = u_rid
            item['ugc_day'] = u_day
            item['ugc_type'] = u_type
            item['ugc_type_r'] = u_type_r
            item['ugc_crawl_time'] = u_date

            yield item
