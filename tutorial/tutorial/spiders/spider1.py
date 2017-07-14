# encoding: utf-8
#-*-coding:utf-8-*-
'''
Created on 2017年7月10日

@author: David
'''

import scrapy


class Spider(scrapy.Spider):
    name = "billy"

    def start_requests(self):
        urls = [
            #'http://www.jikexueyuan.com/course/pythonbase/'
            'http://dmoztools.net/'
          
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]  
        filename = 'billy-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
class Spider1(scrapy.Spider):
    name = "quote"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quote-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)
        
class Spider2(scrapy.Spider):
    name='spider2'
    
    def start_requests(self):
        urls=[
            'https://www.ibm.com/developerworks/cn/opensource/os-cn-tourofgit/index.html'
            ]
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
        
        def parse(self,response):
            page = response.url.split("/")[-2]
            filename = 'spider2-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Save file %s' % filename)
   
#import sys
#sys.path.append("..")
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        'http://dmoztools.net/'
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    def parse(self, response):
        '''
        page = response.url.split("/")[-2]
        filename = 'dmoz-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)
        '''
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
   