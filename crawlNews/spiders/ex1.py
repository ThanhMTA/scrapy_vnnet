import scrapy


class MySpider(scrapy.Spider):
    name = "example.com"
   
    start_urls = [
       "https://e.vnexpress.net/news/news"
       
    ]

    def parse(self, response):
        for href in response.css("h2.title_news_site > a::attr(href)").getall():
            yield scrapy.Request(response.urljoin(href), self.news)
    def news (self, response):
        item = {
            "title":response.css("h1.title_post::text").get()
        }
        yield item

    

       