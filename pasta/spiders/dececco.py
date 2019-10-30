import scrapy, json, re

class DeCeccoSpider(scrapy.Spider):

    name = "De Cecco"
    domain = "https://www.dececco.com"
    allowed_domains = ["www.dececco.com","dececco.com"]
    time_pattern = re.compile(r"\d+")
    start_urls = [
        "https://www.dececco.com/it_it/products/pasta-di-semola/",
        "https://www.dececco.com/it_it/products/pasta-alluovo/",
        "https://www.dececco.com/it_it/products/paste-speciali/",
        "https://www.dececco.com/it_it/products/prodotti-integrali/",
        "https://www.dececco.com/it_it/products/prodotti-bio/"
    ]

    def parse(self, response):
        for href in response.css(".products > li > a::attr(href)"):
            yield response.follow(href, self.parse_product)

    def parse_product(self, response):
        yield {
            "producer": self.name,
            "line": "",
            "name": response.css("scheda__hero__title::text").get(default=""),
            "type": "",
            "time": self.extract_time(response.css(".infolist::text").get(default="")),
            "url": response.request.url,
            "image": response.css(".scheda__hero__image > img::attr(src)").get(default="")
        }

    def extract_time(self, s):
        try:
            return int(self.time_pattern.search(s).group())
        except:
            return 0
