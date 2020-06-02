# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiliCrawlItem(scrapy.Item):
    """Default"""
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UgcItem(scrapy.Item):
    """
    UGC 全站榜，原创榜和新人榜
    {name: "全站",rid: 0},
    {name: "动画",rid: 1},
    {name: "国创相关",rid: 168}, # rookie没有
    {name: "音乐",rid: 3},
    {name: "舞蹈",rid: 129},
    {name: "游戏",rid: 4},
    {name: "科技",rid: 36},
    {name: "数码",rid: 188},
    {name: "生活",rid: 160},
    {name: "鬼畜",rid: 119},
    {name: "时尚",rid: 155},
    {name: "娱乐",rid: 5},
    {name: "影视",rid: 181}
    day:
    {name: "日排行",value: 1},
    {name: "三日排行",value: 3},
    {name: "周排行",value: 7},
    {name: "月排行",value: 30}
    type:
    {name: "全站榜",value: 'all',type:1},
    {name: "原创榜",value: 'origin',type:2},
    {name: "新人榜",value: 'rookie',type:3}
    rank_type:
    {name: "全部投稿",value: 0},
    {name: "近期投稿",value: 1} # rookie没有
    """
    # domain:https://api.bilibili.com
    # 通过 /x/web-interface/ranking?rid={rid}}&day={day}&type={type}&arc_type={rank_type}&jsonp=jsonp 可获取
    # json['data']['list']
    ugc_aid = scrapy.Field()  # 视频数字ID
    ugc_bvid = scrapy.Field()  # 视频字符串ID
    ugc_author = scrapy.Field()  # 视频作者
    ugc_coins = scrapy.Field()  # 视频投币数
    ugc_duration = scrapy.Field()  # 视频总时长
    ugc_mid = scrapy.Field()  # 视频作者ID
    ugc_image = scrapy.Field()  # 视频图片url
    ugc_play = scrapy.Field()  # 视频播放数
    ugc_pts = scrapy.Field()  # 视频综合得分
    ugc_title = scrapy.Field()  # 视频标题
    ugc_review = scrapy.Field()  # 视频弹幕数
    ugc_rank = scrapy.Field()  # 视频排行
    # 抓取分类信息
    ugc_area = scrapy.Field()  # 视频分类
    ugc_day = scrapy.Field()  # 统计时间
    ugc_type = scrapy.Field()  # 排行榜大类
    ugc_type_r = scrapy.Field()  # 投稿时间分类


class PgcItem(scrapy.Item):
    """
    PGC 新番榜和影视榜
    {name: "番剧", season_type: 1},
    {name: "国产动画", season_type: 4},
    {name: "纪录片", season_type: 3},
    {name: "电影", season_type: 2},
    {name: "电视剧", season_type: 5}
    day:
    {name: "三日排行", value: 3},
    {name: "周排行", value: 7}
    """
    # 通过https://api.bilibili.com/pgc/web/rank/list?day={day}&season_type={season_type}}获取
    # json['result']['list']
    pgc_badge = scrapy.Field()  # 付费范围
    pgc_copyright = scrapy.Field()  # 版权
    pgc_cover = scrapy.Field()  # 封面
    pgc_show = scrapy.Field()  # 信息
    pgc_pts = scrapy.Field()  # 综合评分
    pgc_rank = scrapy.Field()  # 分类下排位
    pgc_sid = scrapy.Field()  # ID
    pgc_danmaku = scrapy.Field()  # 弹幕数
    pgc_follow = scrapy.Field()  # 追剧人数
    pgc_follow_s = scrapy.Field()  # 系列追剧人数
    pgc_view = scrapy.Field()  # 播放量
    pgc_title = scrapy.Field()  # 标题
    # 抓取分类信息
    pgc_type_s = scrapy.Field()  # 影视分类 season_type
    pgc_type_d = scrapy.Field()  # 统计时间 day
