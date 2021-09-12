import os
import sys

from scrapy.cmdline import execute


def r():
    sys.path.append(os.path.dirname(os.path.abspath(
        'database_update/run_scrapy.py')))
    execute(["scrapy", "crawl", "weathers"])
