# -*- coding: utf-8 -*-
import scrapy
from yaobw.items import YaobwItem


# class YaobwSpiderSpider(scrapy.Spider):
#     name = 'yaobw_spider'
#     # allowed_domains = ['www.yaaobw.cn']
#     start_urls = ['http://www.yaobw.cn/yaobw/book.do?flag=show&bookId=1&cid=1&cid2=3']
#
#     base_site = 'http://www.yaobw.cn/yaobw/'
#
#     names = ['info_ym',
#              'info_cf',
#              'info_zf',
#              'info_xz',
#              'info_jb',
#              'info_jc',
#              'info_hljd',
#              'info_gnzz',
#              'info_yfyl',
#              'info_zy',
#              'info_gg',
#              'info_zc']
#
#     labels = {'处方': 1, '制法': 2, '性状': 3, '鉴别': 4, '检查': 5, '含量测定': 6, '功能与主治': 7, '用法与用量': 8, '注意': 9, '规格': 10 , '贮藏': 11, }
#
#     def parse(self, response):
#         yaobw_urls = response.xpath('//tr/td/a[contains(text(), "查看")]/@href').extract()
#
#         for yb_url in yaobw_urls:
#             url = self.base_site + yb_url
#             yield scrapy.Request(url, callback=self.getInfo)
#
#         next_page = response.xpath('/html/body/div[1]/div[3]/div[3]/div[3]/p/a[9]/@href').extract()[0]
#         yield scrapy.Request(self.base_site + next_page, callback=self.parse)
#
#     def getInfo(self, response):
#         item = YaobwItem()
#
#         # 初始化设置为空字符串
#         for i in range(self.names.__len__()):
#             item[self.names[i]] = ''
#
#         # 可以直接提取的信息
#         item['info_ym'] = "<span class='title1'>药名</span>" + response.xpath('/html/body/div[1]/div[3]/div[2]/div[3]/pre/center[1]/b/text()').extract()[0]
#         item['origin_url'] = response.url
#         item['origin_body'] = response.body.decode('utf-8')
#
#         # 主体转化为文本之后，使用正则表达式切割后存储到对应的item中
#         contain = response.xpath('//*[@id="content_text"]/text()')
#         contain_text = ''
#         for text in contain:
#             contain_text += text.extract().strip()
#
#         list = contain_text.split('【')
#
#         # 查看是否在所需要的标签列表中，如果在的话，将信息提取出来
#         for i in range(1, list.__len__()):
#             l = list[i].split('】')[0]
#             c = list[i].split('】')[1]
#             if l in self.labels.keys():
#                 item[self.names[self.labels[l]]] = "<span class = 'title1'>" + l + "</span>" + c
#
#         yield item

#
class YaobwSpiderSpider(scrapy.Spider):
    name = 'yaobw_spider'
    # allowed_domains = ['www.yaaobw.cn']
    start_urls = ['http://www.yaobw.cn/yaobw/book.do?flag=show&bookId=1&cid=1&cid2=1']

    base_site = 'http://www.yaobw.cn/yaobw/'

    names = [
        'info_py',
        'info_ywm',
        'info_xz',
        'info_jb',
        'info_jc',
        'info_jcw',
        'info_hlcd',
        'info_pz',
        'info_xwgj',
        'info_gnzz',
        'info_yfyl',
        'info_zy',
        'info_zc',
        'info_ym'
    ]

    labels = {'性状': 2, '鉴别': 3, '检查': 4, '浸出物': 5, '含量测定': 6, '炮制': 7, '性味与归经': 8, '功能与主治': 9, '用法与用量': 10, '注意': 11, '贮藏': 12, '用法与用置': 10 }
    f = open('names.txt', mode='w')

    def parse(self, response):
        yaobw_urls = response.xpath('//tr/td/a[contains(text(), "查看")]/@href').extract()

        for yb_url in yaobw_urls:
            url = self.base_site + yb_url
            yield scrapy.Request(url, callback=self.getInfo)

        next_page = response.xpath('/html/body/div[1]/div[3]/div[3]/div[3]/p/a[contains(text(), "下一页")]/@href').extract()[0]
        yield scrapy.Request(self.base_site + next_page, callback=self.parse)

    def getInfo(self, response):
        item = YaobwItem()

        # 初始化设置为空字符串
        for i in range(self.names.__len__()):
            item[self.names[i]] = ''

        # 可以直接提取的信息
        item['info_ym'] = "<span class='title_1'>药名</span>" + response.xpath('/html/body/div[1]/div[3]/div[2]/div[3]/pre/center[1]/b/text()').extract()[0]
        item['info_py'] = "<span class='title_1'>拼音</span>" + \
                          response.xpath('/html/body/div[1]/div[3]/div[2]/div[3]/pre/center[2]/b/text()').extract()[0]
        item['info_ywm'] = "<span class='title_1'>英文名</span>" + \
                          response.xpath('/html/body/div[1]/div[3]/div[2]/div[3]/pre/center[3]/b/text()').extract()[0]

        item['origin_url'] = response.url
        item['origin_body'] = response.body.decode('utf-8')

        # 主体转化为文本之后，使用正则表达式切割后存储到对应的item中
        contain = response.xpath('//*[@id="content_text"]/text()')
        contain_text = ''
        for text in contain:
            contain_text += text.extract().strip()

        list = contain_text.split('【')

        # 查看是否在所需要的标签列表中，如果在的话，将信息提取出来
        for i in range(1, list.__len__()):
            l = list[i].split('】')[0]
            c = list[i].split('】')[1]
            if l in self.labels.keys():
                item[self.names[self.labels[l]]] = "<span class = 'title_1'>" + l + "</span>" + c
            else:
                print(l)
                self.f.write(l + '\r\n')

        yield item


