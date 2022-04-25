import scrapy
from NBA.items import NbaItem

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/NBA/index6504.html']

    def parse(self, response):
        targets = response.css("div.r-list-container.action-bar-margin.bbs-screen > div.r-ent")
        for t in targets:
            data = NbaItem()
            try:
                num = t.css("div.nrec > span::text").get()
                if num == "爆":
                    data["num"] = 100
                else:
                    data["num"] = int(num)
            except:
                data["num"] = 0
            data["link"] = t.css("div.title > a::attr(href)").get()
            if data["link"] is not None:
                data["link"] = data["link"].strip()
            data["title"] = t.css("div.title > a::text").get()
            if data["title"] is not None:
                data["title"] = data["title"].strip()
            data["author"] = t.css("div.meta > div.author::text").get()
            if data["author"] is not None:
                data["author"] = data["author"].strip()
            data["date"] = t.css("div.meta > div.date::text").get()
            yield data

        next_page = response.css("div.btn-group.btn-group-paging > a:nth-child(2)::attr(href)").get().strip()
        yield response.follow(response.urljoin(next_page), callback=self.parse)
        
