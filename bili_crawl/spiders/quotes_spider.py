<<<<<<< HEAD
"""
根据Scrapy的教程测试
"""
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a python module """

__author__ = 'Jack Zhang'

>>>>>>> ff71efa58df73330fc3dcebeb7153b65f65a269d
import scrapy


class QuotesSpider(scrapy.Spider):
<<<<<<< HEAD
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
=======
    # name identifies the Spider
    name = 'quotes'

    # def start_requests(self):
    #     urls = ['http://quotes.toscrape.com/page/1',
    #             'http://quotes.toscrape.com/page/2']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # can just define a start_urls class attribute with a list of URLs. This list will then be used by the
    # default implementation of start_requests() to create the initial requests for this spider
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # parse() is Scrapy’s default callback method, which is called for requests without an explicitly assigned callback
    def parse(self, response):
        # print('>>>>Response URL:', response.url.split('/'))
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
>>>>>>> ff71efa58df73330fc3dcebeb7153b65f65a269d
