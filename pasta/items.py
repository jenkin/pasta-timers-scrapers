# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PastaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    producer = scrapy.Field()
    line = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
