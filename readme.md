# Manga Scraper

Manga scraper.

Supported websites:

* [MangaPanda](https://mangapanda.org/)
* [MangaHere](http://www.mangahere.cc/)

## Installation

What needs to be installed and configured?

* Python 3
* Docker
* virtualenv

First, initiate the virtualenv environment.

```bash
virtualenv -p python3 env
source env/bin/activate
```

And then install the requirements.

```
pip install -r requirements.txt
```

Then, pull the docker image for [Splash](https://github.com/scrapinghub/splash) and run it.

```
docker pull scrapinghub/splash
docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash
```

Now, just start scrapping 😀

### Notes for kindle users and automatic MOBI conversion

To be able to use the pipeline that automatically converts the scrapped images
to the MOBI format (kindle format) you need to install the [Kindle Comic Converter](https://github.com/ciromattia/kcc),
so you may want to do that before running the crawler.
