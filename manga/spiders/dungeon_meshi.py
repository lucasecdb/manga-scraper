# -*- coding: utf-8 -*-
import scrapy

from manga.spiders.base import MangaPandaBaseSpider


class DungeonMeshiSpider(MangaPandaBaseSpider):
    name = 'dungeon_meshi'
    start_urls = ['https://mangapanda.org/manga/dungeon-meshi/']
