# -*- coding: utf-8 -*-
# import sys
# reload(sys)
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from md999.items import Md999Item

# sys.setdefaultencoding('utf-8')

class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['999.md']
    start_urls = ['https://www.999.md/']

    rules = (
        Rule(LinkExtractor(allow=r'\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = Md999Item()
        i['name'] = str(response.xpath('//h1[@itemprop = "name"]/text()').extract()).encode('utf-8')
        i['phone'] = str(response.xpath('//strong/text()').extract()).encode('utf-8')
        i['description'] = str(response.xpath('//div[@itemprop="description"]/text()').extract()).encode('utf-8')
        with open("rezultat.txt", "a" ) as f:
            phone = u"%s" % i['phone']
            name = u"%s" % i['name']
            description = u"%s" % i['description']
            f.write(name+'\n')
            f.write(description+'\n')
            f.write(phone+'\n')
            f.close()
            print repr(i)
