import scrapy
import scrapy_splash


class MangaPandaBaseSpider(scrapy.Spider):
    allowed_domains = ['mangapanda.org', 'cdn.mgid.com']

    def parse(self, response):
        def get_chapter_nums(a):
            n = []

            for i in range(len(a)):
                if (i + 1) % 2 == 0:
                    n[-1] += a[i]
                else:
                    n.append(a[i])

            return n

        links = response.xpath(
            '//li[contains(@class, "list-group-item")]/a/@href'
        ).extract()

        chapter_numbers = get_chapter_nums(response.xpath(
            '//li[contains(@class, "list-group-item")]//*[contains(@class, "_3D1SJ")]/text()'
        ).extract())

        for i in range(len(links)):
            link = links[i]
            chapter = 'Chapter %s' % chapter_numbers[i]

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
