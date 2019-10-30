import scrapy, json, re

class BarillaSpider(scrapy.Spider):

    name = "Barilla"
    domain = "https://www.barilla.com"
    allowed_domains = ["www.barilla.com","barilla.com"]
    time_pattern = re.compile(r"\d+")
    start_urls = [
        "https://www.barilla.com/it-it/data/productresults/get?h=-1947067082&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=1942467834&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=1602631109&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=1846876971&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=2131218998&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=52490792&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=511675135&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=1639782577&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=-1164285014&sort=alpha",
        "https://www.barilla.com/it-it/data/productresults/get?h=1663885353&sort=alpha"
    ]

    def parse(self, response):
        payload = json.loads(response.text)
        for product in payload["results"]:
            yield {
                "producer": self.name,
                "line": product["range"],
                "name": product["title"],
                "type": "",
                "time": self.extract_time(product["cookingTime"]),
                "url": "%s%s" % (self.domain, product["url"]),
                "image": product["packShot"]
            }

    def extract_time(self, s):
        try:
            return int(self.time_pattern.search(s).group())
        except:
            return 0
