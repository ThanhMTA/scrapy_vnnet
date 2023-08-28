# import scrapy 
# from  crawlNews.items import CrawlnewsItem

# class MycrawlBaoMoi (scrapy.Spider):
#     name="baomoi"
#     # allowed_domains = ["web"]
#     start_urls = ( 
#         'https://dantri.com.vn/the-gioi.htm', 
#     )
    
#     def parse(self, response):
       
#         for href in response.css("article>div>h3>a::attr(href)").getall():
            
#             yield scrapy.Request(response.urljoin(href), self.news)
#         href = response.css("a.next::attr(href)").extract_first()
#         if href:
#             yield scrapy.Request(response.urljoin(href), self.parse)
     
#     def news (self, response):
#         yield {
           
#                 "title": response.css('h1::text').get(),
                
#             }
        
import scrapy 
from crawlNews.items import CrawlnewsItem

class MycrawlBaoMoi(scrapy.Spider):
    name = "baomoi"
    start_urls = (
        'https://dantri.com.vn/the-gioi.htm',
    )

    def parse(self, response):
        # for href in response.css("article>div>h3>a::attr(href)").getall():
        #     yield scrapy.Request(response.urljoin(href), callback=self.news)
        next_page = response.css("a.next::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def news(self, response):
        yield {
            "title": response.css('h1::text').get(),
        }
