# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class YaobwPipeline(object):

    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='mydb', charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        # self.cursor.execute(
        #     """insert into nanshezi(
        #         title, content, body, url, comment, pub_time, read_times, classic, labels
        #     ) value (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        #     (
        #         item['title'],
        #         item['content'],
        #         item['body'],
        #         item['url'],
        #         item['comment'],
        #         item['pub_time'],
        #         item['read_times'],
        #         item['classic'],
        #         item['labels']
        #     )
        # )
        # self.connection.commit()
        return item

    def __del__(self):
        self.cursor.close()
        self.connection.close()

