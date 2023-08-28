import scrapy 
from  crawlNews.items import CrawlnewsItem

from urllib import parse
class MycrawlBaoMoi (scrapy.Spider):
    name="next"
  
    start_urls = [
       "https://dantri.com.vn/the-gioi.htm"
       
    ]
    
    def parse(self, response):
        next = response.css("a.page-item::attr(href)")
        for href in response.css("a.page-item::attr(href)").getall():
            yield scrapy.Request(parse.urljoin(response.url, href), self.parse,True)
        item_selectors = response.css('article>div>a::attr(href)') 
        for href in item_selectors.extract():
        # for href in response.css("article>div>a::attr(href)").getall():     
            yield scrapy.Request(parse.urljoin(response.url,href), self.news, True)
    
                  
    def news (self, response):
 
    
        # yield scrapy.Request(response.urljoin(response.css("div.author-name >a::attr(href)").get()), self.author)
        yield {
             
                 "title":response.css("article>h1::text").get()
                     }
    