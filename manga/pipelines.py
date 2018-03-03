import scrapy
import logging

from os import path, listdir, rename
from scrapy.pipelines.images import ImagesPipeline
from manga.settings import IMAGES_STORE
from subprocess import STDOUT, PIPE
from psutil import Popen, TimeoutExpired


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


class MobiConverterPipeline(object):

    def process_item(self, item, spider):
        pass

    def close_spider(self, spider):
        logger = logging.getLogger()

        logger.info('Starting MOBI generation of scrapped images')

        storage = IMAGES_STORE
        folder_name = spider.folder_name

        results_path = path.abspath(path.join(storage, folder_name))

        chapter_directories = listdir(results_path)

        for i in range(len(chapter_directories)):
            chapter_directory = chapter_directories[i]

            logger.info('Generating MOBI file for %s (%d/%d)' %
                        (chapter_directory, i + 1, len(chapter_directories)))

            chapter_number = ""

            if '.' in chapter_directory:
                chapter_number = "##%05.1f" % float(chapter_directory)
            else:
                chapter_number = "#%03d" % int(chapter_directory)

            chapter_title = folder_name + " " + chapter_number

            pipe = Popen('kcc-c2e -m -p KPW --whiteborders -f MOBI -u -r 2 -t "%s" "%s"' %
                         (chapter_title,
                          path.join(results_path, chapter_directory)),
                         stdout=PIPE, stderr=STDOUT, stdin=PIPE, shell=True)

            try:
                pipe.wait(60)

                generated_file_name = path.join(
                    results_path, chapter_directory) + ".mobi"
                rename(generated_file_name, path.join(results_path,
                                                      chapter_title) + ".mobi")

                logger.info('MOBI file generated successfully')
            except TimeoutExpired:
                logger.error('Unable to generate MOBI file for %s' %
                             (chapter_directory))

        logger.info('Finalized MOBI generation of scrapped images')
