import threading
from queue import Queue
from spider import Spider
from domain import *
from crawler import *

PROJECT_NAME = 'thesite'
HOMEPAGE = 'http://dazzlingschoolpune.in/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWL_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
