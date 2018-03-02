# -*- coding: utf-8 -*-
import scrapy

from manga.spiders.base import MangaPandaBaseSpider


class FairyTailSpider(MangaPandaBaseSpider):
    name = 'fairy_tail'
    folder_name = 'Fairy Tail'
    start_urls = ['https://mangapanda.org/manga/fairy-tail_110']
