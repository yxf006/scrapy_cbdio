# -*- coding: utf-8 -*-
import scrapy
from test1.items import Test1Item
from scrapy.selector import Selector
from scrapy import Request
#import json

class CbdioSpider(scrapy.Spider):
    name = "cbdio"
    #allowed_domains = ["http://www.cbdio.com"]
    start_urls = (
        'http://www.cbdio.com/',
    )

    url_prefix='http://www.cbdio.com/'

    def parse(self, response):
        selector=Selector(response)
        #titles=selector1.xpath('/html/body/div[4]/div[2]/div[1]/div[3]/ul/li[1]/div/p[1]/a')

        #newslist=selector.css('body > div.am-container.cb-main > div.am-g > div.am-u-md-8 > div:nth-child(4) > ul > li:nth-child(n) > div > p.cb-media-title > a').extract()
        newslist=selector.css('body > div.am-container.cb-main > div.am-g > div.am-u-md-8 > div:nth-child(4) > ul > li:nth-child(n) ')
        #items=[]
        for each in newslist:
            item=Test1Item()
            item['title']=each.css('div > p.cb-media-title > a').xpath('text()').extract()[0]
            #item['title']=json.JSONEncoder(each,ensure_ascii=False)
            item['url']=self.url_prefix+each.css('div > p.cb-media-title > a').xpath('@href').extract()[0]
            item['summary']=each.css('div > p.cb-media-summary').xpath('text()').extract()[0]
            content_url=item['url']
            yield Request(url=content_url,meta={'item':item},callback=self.parse_content)

            #f=file("/tmp/feeds/test.res","a")
            #f.write(each.encode('utf-8'))
            #f.close()
            #items.append(item)
            #yield  item

    def parse_content(self,response):
        if response.status==200:
            item=response.meta['item']
            selector=Selector(response)
            content=selector.css('body > div.am-container.cb-main > div.am-g > div.am-u-md-8').extract()[0]#.encode('utf-8')
            #print('parse_content=',content)
            item['content']=content
            yield item

