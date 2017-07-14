# -*- coding: utf-8 -*-
import scrapy


class KylinaxMeSpider(scrapy.Spider):
    name = 'kylinax.me'
    allowed_domains = ['www.kylinax.me']
    start_urls = ['http://www.kylinax.me/']

    def parse(self, response):
        pass
