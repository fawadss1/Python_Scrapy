# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class ProjectPipeline(object):

    def __init__(self):
        self.curr = None
        self.conn = None
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='books_scrap'
        )
        self.curr = self.conn.cursor()

    def process_item(self, book, spider):
        self.save_data(book)
        return book

    def save_data(self, book):
        self.curr.execute(""" insert into books_data values (%s, %s, %s, %s, %s) """,
                          (book['Title'],
                           book['Price'],
                           book['Currency_Symbol'],
                           book['Stock_Status'],
                           book['Url']
                           ))
        self.conn.commit()
