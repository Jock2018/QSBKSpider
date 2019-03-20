# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义要储存的字段
class DuanZi(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page = scrapy.Field()
    user_name = scrapy.Field()
    user_age = scrapy.Field()
    user_gender = scrapy.Field()
    user_content = scrapy.Field()
    laught_number = scrapy.Field()
    comment_number = scrapy.Field()