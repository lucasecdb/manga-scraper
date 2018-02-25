# -*- coding: utf-8 -*-
import scrapy
from manga.spiders.base import MangaHereBaseSpider


class DungeonMeshiMangahereSpider(MangaHereBaseSpider):
    name = 'dungeon_meshi_mangahere'
    start_urls = ['http://www.mangahere.cc/manga/dungeon_meshi/']
