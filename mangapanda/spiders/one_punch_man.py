# -*- coding: utf-8 -*-
import scrapy

from mangapanda.spiders.base_spider import BaseSpider


class OnePunchManSpider(BaseSpider):
    name = 'one_punch_man'
    allowed_domains = ['mangapanda.org', 'cdn.mgid.com']
    start_urls = ['https://mangapanda.org/manga/onepunch-man_103']
