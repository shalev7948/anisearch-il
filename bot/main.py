import time
from scrapers.test_scraper import run as scrape
from bot.notify import run as notify

while True:
    scrape()
    notify()
    print("RUNNING...")
    time.sleep(300)
