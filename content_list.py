#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   content_list.py
@Author  :   zgc_jack
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/5/30 14:31    1.0         None

describe:内容list
"""

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

# 输出 url_list
url_list = []

# type 使用0, time 使用7
for pic in topic_list:
    channels = pic.get('channels')
    rank = pic.get('name')
    for channel in channels:
        tid = channel.get('tid')
        url = '%s/%s/%s/%s/%s' % (_domain, rank, tid, 0, 7)
        url_list.append(url)


if __name__ == '__main__':
    print(url_list)
