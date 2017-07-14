# encoding: utf-8
#-*-coding:utf-8-*-
'''
Created on 2017年7月10日

@author: David
'''

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''
html = etree.HTML(text)
#result = etree.tostring(html)
result=html.xpath('//li')
print(len(result))
print(type(result))
print(type(result[0]))

'''
from scrapy.spider import BaseSpider

class Spider1(BaseSpider):
    name="billy"
    allow_domains=["bilibili.com"]
    start_urls=["http://www.bilibili.com"]
    
    
    def parse(self,response):
        filename=response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
'''

'''
from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        '''