#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a python module """

__author__ = 'Jack Zhang'

import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


configure_logging()
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    yield runner.crawl('bili_ugc')
    yield runner.crawl('bili_pgc')
    reactor.stop()


crawl()
reactor.run()
