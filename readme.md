# MangaPanda Scraper

Scraper for the MangaPanda [website](https://mangapanda.org/).

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
