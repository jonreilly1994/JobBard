from django.core.management.base import BaseCommand,CommandError
from JobScraping.TwitterScraper import TwitterScraper
import os

class Command(BaseCommand):
    help = "Loads jobs from files into DB"

    def handle(self, *args, **options):
        url = "https://careers.twitter.com/content/careers-twitter/en/jobs-search.html?q=software&start="
        urls = []
        for x in range(5):
            urls.append(url + str(x*10))

        twitterScraper = TwitterScraper()
        #input_file = "C:\\Users\Jon\Desktop\JobJolt\Code\JobJolt\JobBard\jobboard\scrape_tests/twitter.html"
        #print(input_file)
        #twitterScraper.openFile(input_file)
        #twitterScraper.scrape()

        for u in urls:
           print("Scraping: " + u)
           twitterScraper.openUrl(u)
           twitterScraper.scrape()
