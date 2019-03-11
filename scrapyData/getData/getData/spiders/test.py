import scrapy
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        # "https://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "https://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # "https://www.baidu.com/"
        "http://caipiao.163.com/"
    ]

    def parse(self, response):
        # print(response.body, "+++++")
        filename = response.url.split("/")[-2]
        with open("../getData/data/" + filename + ".txt", 'wb') as f:
            f.write(response.body)
