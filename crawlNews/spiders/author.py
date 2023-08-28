import scrapy 
from  crawlNews.items import CrawlnewsItem

class MycrawlBaoMoi (scrapy.Spider):
    name="author"
    # allowed_domains = ["web"]
    start_urls = ( 
        'http://quotes.toscrape.com/', 
    )
    
    def parse(self, response):
       
        for href in response.css("span>a::attr(href)").getall():
            
            yield scrapy.Request(response.urljoin(href), self.news)
        href = response.css("li.next >a::attr(href)").extract_first()
        if href:
            yield scrapy.Request(response.urljoin(href), self.parse)
     
    def news (self, response):
        yield {
           
                "author": response.css('h3.author-title::text').get(),
                "born":response.css('span.author-born-date::text').get()
            }
        