# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LolspiderItem(scrapy.Item):
    # define the fields for your item here like:
    heros_name = scrapy.Field()
    heros_nickname = scrapy.Field()
    heros_type = scrapy.Field()
    Physical = scrapy.Field()
    magic = scrapy.Field()
    defense = scrapy.Field()
    difficulty = scrapy.Field()
    wallpaper = scrapy.Field()
    imgname = scrapy.Field()
    Background_story = scrapy.Field()

