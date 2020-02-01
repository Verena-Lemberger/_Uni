import scrapy


class mobySpider(scrapy.Spider):
    name = "moby"

    def start_requests(self):
        start_urls = ["https://www.gutenberg.org/files/2701/2701-h/2701-h.htm"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'moby.html'
        with open(filename, 'wb') as f:
            f.write(response.body)