import scrapy
from ..items import ProjectItem
import re


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        book = ProjectItem()
        cards = response.css("article.product_pod")
        for i in cards:
            if i.xpath("//p[@class='instock availability']//i[@class='icon-ok']").get() is not None:
                stockStatus = "In-Stock"
            else:
                stockStatus = "Not Available"
            title = i.css("h3 a::text").get()
            price = i.css("div.product_price p.price_color::text").get()
            url = i.css("h3 a::attr('href')").get()

            number = re.findall(r'\d+', price)[0]
            symbol = re.findall(r'[^\d]+', price)[0]

            if symbol == '€':
                short_name = 'EUR'
            elif symbol == '£':
                short_name = 'GBP'
            else:
                short_name = 'Unknown'

            book['Title'] = title
            book['Price'] = number
            book['Currency_Symbol'] = short_name
            book['Stock_Status'] = stockStatus
            book['Url'] = url

            yield book

            nextPage = response.css("li.next a::attr('href')").get()
            if nextPage is not None:
                yield response.follow(nextPage, self.parse)