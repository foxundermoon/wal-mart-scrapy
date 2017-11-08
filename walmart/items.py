# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WalmartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area= scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
    openTime = scrapy.Field()
    isSanm = scrapy.Field()
    pass
