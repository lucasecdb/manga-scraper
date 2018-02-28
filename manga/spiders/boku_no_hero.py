# -*- coding: utf-8 -*-
import scrapy
from manga.spiders.base import MangaPandaBaseSpider


class BokuNoHeroSpider(MangaPandaBaseSpider):
    name = 'boku_no_hero'
    folder_name = 'Boku no Hero Academia'
    start_urls = ['https://mangapanda.org/manga/boku-no-hero-academia_104']
