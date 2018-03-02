import scrapy
import scrapy_splash


class MangaPandaBaseSpider(scrapy.Spider):
    allowed_domains = ['mangapanda.org', 'cdn.mgid.com']

    def parse(self, response):
        links = response.xpath(
            '//li[contains(@class, "list-group-item")]/a/@href'
        ).extract()

        chapters_raw = response.xpath(
            '//li[contains(@class, "list-group-item")]//*[contains(@class, "_3D1SJ")]/text()'
        ).extract()

        chapter_numbers = [chapters_raw[i]
                           for i in range(len(chapters_raw)) if i % 2 != 0]

        for i in range(len(links)):
            link = links[i]
            chapter = chapter_numbers[i]

            yield scrapy_splash.SplashRequest(link, self.parse_chapter_page, args={
                'wait': 5
            }, meta={
                'chapter': chapter
            })

    def parse_chapter_page(self, response):
        image_links = response.xpath(
            '//*[@id="mangareader"]/div[1]//img[@class="PB0mN"]/@src').extract()

        yield {
            'image_urls': image_links,
            'chapter': response.meta['chapter']
        }


class MangaHereBaseSpider(scrapy.Spider):
    allowed_domains = ['mangahere.cc']

    def parse(self, response):
        links = response.xpath(
            '//*[@class="manga_detail"]/*[@class="detail_list"]/ul/li//a/@href').extract()

        chapters = response.xpath(
            '//*[@class="manga_detail"]/*[@class="detail_list"]/ul/li//a/text()'
        ).extract()

        for i in range(len(links)):
            link = 'http:' + links[i]
            chapter = chapters[i].strip()

            yield scrapy.Request(link, meta={'chapter': chapter}, callback=self.parse_chapter_page)

    def parse_chapter_page(self, response):
        image_link = response.xpath(
            '//*[@id="viewer"]/a/img[2]/@src').extract_first()

        title = response.xpath(
            '//*[@class="readpage_top"]/div[@class="title"]/span/text()').extract_first().strip()

        next_page = 'http:' + \
            response.xpath('//*[@id="viewer"]/a/@href').extract_first()

        yield {
            'image_urls': [image_link],
            'image_names': [title],
            'chapter': response.meta['chapter']
        }

        if next_page != 'javascript:void(0);':
            yield scrapy.Request(next_page, meta=response.meta, callback=self.parse_chapter_page)
