import scrapy
from scrapy.pipelines.images import ImagesPipeline


class MangaImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image_urls = item.get('image_urls', [])
        image_names = item.get(
            'image_names', [i + 1 for i in range(len(image_urls))])

        for i in range(len(image_urls)):
            url = image_urls[i]
            name = image_names[i]

            yield scrapy.Request(url, meta={
                'folder': info.spider.folder_name,
                'chapter': item['chapter'],
                'name': name
            })

    def file_path(self, request, response=None, info=None):
        return '%s/%s/%02d.jpg' % (request.meta['folder'], request.meta['chapter'], request.meta['name'])
