import scrapy, json, re

class GarofaloSpider(scrapy.Spider):

    name = "Garofalo"
    domain = "https://www.pasta-garofalo.com"
    allowed_domains = ["www.pasta-garofalo.com","pasta-garofalo.com"]
    time_pattern = re.compile(r"\d+")
    start_urls = [
        "https://www.pasta-garofalo.com/it/prodotti/pasta-di-semola-di-grano-duro/",
        "https://www.pasta-garofalo.com/it/prodotti/la-giostra-dei-bambini/",
        "https://www.pasta-garofalo.com/it/prodotti/pasta-integrale-biologica/",
        "https://www.pasta-garofalo.com/it/prodotti/pasta-senza-glutine/",
        "https://www.pasta-garofalo.com/it/prodotti/pasta-legumi-e-cereali/",
        "https://www.pasta-garofalo.com/it/prodotti/tanto-per-cambiare-latipica-cucina-italiana/",
        "https://www.pasta-garofalo.com/it/prodotti/pasta-fresca-pasta-garofalo/",
        "https://www.pasta-garofalo.com/it/prodotti/gnocchi/"
    ]

    def parse(self, response):
        for href in response.css(".product-preview-box .img-uri::attr(href)"):
            yield response.follow(href, self.parse_product)

    def parse_product(self, response):
        yield {
            "producer": self.name,
            "line": response.css("#content > section > div:nth-child(1) > div.row.wow.fadeInUp > div > div > ul > li:nth-child(3) > p::text").get(default=""),
            "name": response.css("#content > section > div:nth-child(1) > div.row.content-product > div:nth-child(1) > h1::text").get(default=""),
            "type": response.css("#content > section > div:nth-child(1) > div.row.content-product > div:nth-child(1) > blockquote > a:nth-child(2)::text").get(default=""),
            "time": self.extract_time(response.css("#content > section > div:nth-child(1) > div.row.wow.fadeInUp > div > div > ul > li:nth-child(1) > p::text").get(default="")),
            "url": response.request.url,
            "image": response.css("#content > section > div:nth-child(1) > div.row.content-product > div.col-sm-6.hidden-xs.wow.fadeInUp > img::attr(src)").get(default="")
        }

    def extract_time(self, s):
        try:
            return int(self.time_pattern.search(s).group())
        except:
            return 0
