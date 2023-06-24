from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlingSpider(CrawlSpider):
    name = "myCrawler"
    allowed_domains = ["vixen.com"]
    start_url = ["https://vixen.com/videos"]
    rules = (
        Rule(LinkExtractor(allow="?page=")),
    )
