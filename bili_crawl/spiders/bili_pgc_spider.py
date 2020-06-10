# -*- coding: utf-8 -*-
import scrapy
import json
import time
from bili_crawl.items import PgcItem
from content_list import ContentList
from urllib import parse


class BiliPgcSpiderSpider(scrapy.Spider):
    name = 'bili_pgc'
    url_list = ContentList().pgc_uri
    allowed_domains = ['api.bilibili.com']
    start_urls = url_list[:]
    custom_settings = {
        'ITEM_PIPELINES': {
            'bili_crawl.pipelines.BiliPgcPipeline': 210
        }
    }

    def parse(self, response):
        body = response.body.decode('utf8')
        c_list = json.loads(body)['result']['list']
        params = parse.parse_qs(parse.urlparse(response.url).query)
        p_season = params['season_type'][0]
        p_day = params['day'][0]
        p_date = time.strftime("%Y-%m-%d", time.localtime())

        for c in c_list:
            pItem = PgcItem()
            pItem['pgc_badge'] = c['badge'] if len(c['badge']) else '普通'
            pItem['pgc_copyright'] = c['copyright']
            pItem['pgc_cover'] = c['cover']
            pItem['pgc_show'] = c['new_ep']['index_show']
            pItem['pgc_pts'] = c['pts']
            pItem['pgc_rank'] = c['rank']
            pItem['pgc_sid'] = c['season_id']
            pItem['pgc_danmaku'] = c['stat']['danmaku']
            pItem['pgc_follow'] = c['stat']['follow']
            pItem['pgc_follow_s'] = c['stat']['series_follow']
            pItem['pgc_view'] = c['stat']['view']
            pItem['pgc_title'] = c['title']
            pItem['pgc_type_s'] = p_season
            pItem['pgc_type_d'] = p_day
            pItem['pgc_crawl_time'] = p_date

            yield pItem
