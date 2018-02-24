# -*- coding: utf-8 -*-
import scrapy

from manga.spiders.base import MangaPandaBaseSpider


class OnePunchManSpider(MangaPandaBaseSpider):
    name = 'one_punch_man'
    start_urls = ['https://mangapanda.org/manga/onepunch-man_103']
