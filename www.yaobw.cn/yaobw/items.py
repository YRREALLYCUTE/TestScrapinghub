# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YaobwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 中成药部分
    info_ym = scrapy.Field()
    info_cf = scrapy.Field()
    info_zf = scrapy.Field()
    info_xz = scrapy.Field()
    info_jb = scrapy.Field()
    info_jc = scrapy.Field()
    info_hljd = scrapy.Field()
    info_gnzz = scrapy.Field()
    info_yfyl = scrapy.Field()
    info_zy = scrapy.Field()
    info_gg = scrapy.Field()
    info_zc = scrapy.Field()
    origin_url = scrapy.Field()
    origin_body = scrapy.Field()

    info_py = scrapy.Field()
    info_ywm = scrapy.Field()
    info_jcw = scrapy.Field()
    info_hlcd = scrapy.Field()
    info_pz = scrapy.Field()
    info_xwgj = scrapy.Field()


class blogItem(scrapy.Item):
    # 中草药部分
    title = scrapy.Field()
    content = scrapy.Field()
    body = scrapy.Field()
    url = scrapy.Field()
    comment = scrapy.Field()
    pub_time = scrapy.Field()
    read_times = scrapy.Field()
    classic = scrapy.Field()
    labels = scrapy.Field()




