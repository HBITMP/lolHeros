# -*- coding: utf-8 -*-
import logging

import scrapy

from lolspider.items import LolspiderItem


class LolSpider(scrapy.Spider):
    name = 'lol'
    allowed_domains = ['lol.qq.com']
    start_urls = ['http://lol.qq.com/web201310/info-heros.shtml']

    start = 'http://lol.qq.com/web201310/info-heros.shtml'

    def start_requests(self):
        yield scrapy.Request(self.start, callback=self.parse_index)

    def parse_index(self, response):
        heros = response.css('#jSearchHeroDiv li a::attr(href)').extract()
        print(heros)
        for item in heros:
            full_url = response.urljoin(item)
            print(full_url)
            yield scrapy.Request(full_url, callback=self.parse_heros)

    def parse_heros(self, response):
        print (response.text)
        heros_name = response.css('#DATAname::text').extract_first()
        heros_nickname = response.css('#DATAtitle::text').extract_first()
        heros_type = response.css('#DATAtags span::text').extract()
        Physical = response.css('#DATAinfo .up1::attr(title)').extract_first()
        magic = response.css('#DATAinfo .up2::attr(title)').extract_first()
        defense = response.css('#DATAinfo .up3::attr(title)').extract_first()
        difficulty = response.css('#DATAinfo .up4::attr(title)').extract_first()
        wallpaper = response.css('#skinNAV > li > a > img::attr(src)').extract()
        imgname = response.css('#skinNAV > li > a::attr(title)').extract()
        Background_story = response.css('.bgstroy #DATAlore::text').extract_first()

        items = LolspiderItem()
        items['heros_name'] = heros_name
        items['heros_nickname'] = heros_nickname
        items['heros_type'] = heros_type
        items['Physical'] = Physical
        items['magic'] = magic
        items['defense'] = defense
        items['difficulty'] = difficulty
        items['wallpaper'] = wallpaper
        items['imgname'] = imgname
        items['Background_story'] = Background_story
        yield items

