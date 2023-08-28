import scrapy 
from  crawlNews.items import CrawlnewsItem

class MycrawlBaoMoi (scrapy.Spider):
    name="vietnamenet"
    # allowed_domains = ["web"]
    start_urls = ( 
        'https://vietnamnet.vn/chinh-tri', 
    )
    
    def parse(self, response):
       
        for href in response.css("div.mb-20>div>h3>a::attr(href)").getall():
            
            yield scrapy.Request(response.urljoin(href), self.news)
        href = response.css("li.pagination-next >a::attr(href)").extract_first()
        if href:
            yield scrapy.Request(response.urljoin(href), self.parse)
     
    def news (self, response):
        yield {
           
                "title": response.css('h1.content-detail-title::text').get(),
                "author:": response.css('span.name > a::text').get(),
                "content:":response.css(' div#maincontent >p::text').getall(),
               
                
            }
        