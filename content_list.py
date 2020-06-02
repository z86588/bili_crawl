#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   content_list.py
@Author  :   zgc_jack
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/5/30 14:31    1.0         None

describe:页面内容list
"""


class ContentList(object):
    _rankMenu = [
        {'name': "全站榜", 'type': "all"},
        {'name': "原创榜", 'type': "origin"},
        {'name': "新番榜", 'type': "bangumi"},
        {'name': "影视榜", 'type': "cinema"},
        {'name': "新人榜", 'type': "rookie"},
    ]

    # 分类列表
    # all, origin 使用c_list,rookie使用rookie_list
    _c_list = [
        {'name': "全站", 'tid': 0},
        {'name': "动画", 'tid': 1},
        {'name': "国创相关", 'tid': 168},
        {'name': "音乐", 'tid': 3},
        {'name': "舞蹈", 'tid': 129},
        {'name': "游戏", 'tid': 4},
        {'name': "科技", 'tid': 36},
        {'name': "数码", 'tid': 188},
        {'name': "生活", 'tid': 160},
        {'name': "鬼畜", 'tid': 119},
        {'name': "时尚", 'tid': 155},
        {'name': "娱乐", 'tid': 5},
        {'name': "影视", 'tid': 181}
    ]

    _rookie_list = _c_list.copy()
    _rookie_list.pop(2)

    _time_list = [
        {'name': "日排行", 'value': 1},
        {'name': "三日排行", 'value': 3},
        {'name': "周排行", 'value': 7},
        {'name': "月排行", 'value': 30}
    ]

    # 目前没有使用
    _type_list = [
        {'name': '全部投稿', 'value': 0},
        {'name': '近期投稿', 'value': 1},
    ]

    # 汇总榜单列表,爬取用
    # url结构为https://www.bilibili.com/ranking/{_rankMenu.name}/{channel.tid}/{_type_list.value}/{_time_list.value}
    topic_list = [
        {'name': 'all', 'channels': _c_list, 'times': _time_list},
        {'name': 'origin', 'channels': _c_list, 'times': _time_list},
        {'name': 'bangumi', 'channels': [
            {'name': "番剧", 'tid': 13, 'season_type': 1},
            {'name': "国产动画", 'tid': 167, 'season_type': 4}
        ], 'times': [{'name': "三日排行", 'value': 3}, {'name': "周排行", 'value': 7}]},
        {'name': 'cinema', 'channels': [
            {'name': "纪录片", 'tid': 177, 'season_type': 3},
            {'name': "电影", 'tid': 23, 'season_type': 2},
            {'name': "电视剧", 'tid': 11, 'season_type': 5}
        ], 'times': [{'name': "三日排行", 'value': 3}, {'name': "周排行", 'value': 7}]},
        {'name': 'rookie', 'channels': _rookie_list, 'times': _time_list}
    ]

    _domain = 'https://www.bilibili.com/ranking'

    # api使用list
    # PGC
    _pgc_list = [
        {'name': "番剧", 'season_type': 1},
        {'name': "国产动画", 'season_type': 4},
        {'name': "纪录片", 'season_type': 3},
        {'name': "电影", 'season_type': 2},
        {'name': "电视剧", 'season_type': 5},
    ]

    _pgc_day = [
        {'name': "三日排行", 'value': 3},
        {'name': "周排行", 'value': 7},
    ]

    _ugc_list = [
        {'name': "全站", 'rid': 0},
        {'name': "动画", 'rid': 1},
        {'name': "国创相关", 'rid': 168},  # rookie没有
        {'name': "音乐", 'rid': 3},
        {'name': "舞蹈", 'rid': 129},
        {'name': "游戏", 'rid': 4},
        {'name': "科技", 'rid': 36},
        {'name': "数码", 'rid': 188},
        {'name': "生活", 'rid': 160},
        {'name': "鬼畜", 'rid': 119},
        {'name': "时尚", 'rid': 155},
        {'name': "娱乐", 'rid': 5},
        {'name': "影视", 'rid': 181},
    ]

    _ugc_day = [
        {'name': "日排行", 'value': 1},
        {'name': "三日排行", 'value': 3},
        {'name': "周排行", 'value': 7},
        {'name': "月排行", 'value': 30},
    ]

    _ugc_type = [
        {'name': "全站榜", 'value': 'all', 'type': 1},
        {'name': "原创榜", 'value': 'origin', 'type': 2},
        {'name': "新人榜", 'value': 'rookie', 'type': 3},
    ]

    _ugc_rank = [
        {'name': "全部投稿", 'value': 0},
        {'name': "近期投稿", 'value': 1},  # rookie没有
    ]

    _api_domain = 'https://api.bilibili.com'

    # _pgc_uri = f'/pgc/web/rank/list?day={day}&season_type={season_type}'
    # _ugc_uri = f'/x/web-interface/ranking?rid={rid}}&day={day}&type={type}&arc_type={rank_type}&jsonp=jsonp'


if __name__ == '__main__':
    pass
