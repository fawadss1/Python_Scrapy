# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Price = scrapy.Field()
    Currency_Symbol = scrapy.Field()
    Stock_Status = scrapy.Field()
    Url = scrapy.Field()
