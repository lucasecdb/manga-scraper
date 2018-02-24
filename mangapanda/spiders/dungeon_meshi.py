# -*- coding: utf-8 -*-
import scrapy

from mangapanda.spiders.base_spider import BaseSpider


class DungeonMeshiSpider(BaseSpider):
    name = 'dungeon_meshi'
    allowed_domains = ['mangapanda.org', 'cdn.mgid.com']
    start_urls = ['https://mangapanda.org/manga/dungeon-meshi/']
