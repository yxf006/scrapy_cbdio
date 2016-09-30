# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title=scrapy.Field()
	url=scrapy.Field()
	summary=scrapy.Field()
	content=scrapy.Field()
