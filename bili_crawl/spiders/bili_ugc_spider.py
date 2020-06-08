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
            uItem = UgcItem()
            uItem['ugc_bvid'] = c['bvid']
            uItem['ugc_author'] = c['author']
            uItem['ugc_coins'] = c['coins']
            uItem['ugc_duration'] = c['duration']
            uItem['ugc_mid'] = c['mid']
            uItem['ugc_image'] = c['pic']
            uItem['ugc_play'] = c['play']
            uItem['ugc_pts'] = c['pts']
            uItem['ugc_title'] = c['title']
            uItem['ugc_review'] = c['video_review']
            uItem['ugc_rank'] = c_list.index(c)
            uItem['ugc_area'] = u_rid
            uItem['ugc_day'] = u_day
            uItem['ugc_type'] = u_type
            uItem['ugc_type_r'] = u_type_r
            uItem['ugc_time'] = u_date

            yield uItem
