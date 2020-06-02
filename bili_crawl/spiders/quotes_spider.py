#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a python module """

__author__ = 'Jack Zhang'
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'test': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     # next_page = response.urljoin(next_page)
        #     # yield scrapy.Request(next_page, callback=self.parse)
        
        #     yield response.follow(next_page, callback=self.parse)

        # 缩短代码
        # for href in response.css('ul.pager a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)

        # 继续缩短代码
        for a in response.css('ul.pager a'):
            yield response.follow(a, callback=self.parse)
