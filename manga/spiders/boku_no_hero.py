# -*- coding: utf-8 -*-
import scrapy
from manga.spiders.base import MangaPandaBaseSpider


class BokuNoHeroSpider(MangaPandaBaseSpider):
    name = 'boku_no_hero'
    start_urls = ['https://mangapanda.org/manga/boku-no-hero-academia_104']
