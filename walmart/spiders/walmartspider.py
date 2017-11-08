# -*- coding: utf-8 -*-
import scrapy
from walmart.items import WalmartItem


def text(elt):
    txt = elt.xpath('string(.)')[0].root
    return txt.replace('\n','').encode('utf-8')


class WalmartSpider(scrapy.Spider):
    name = 'walmart'
    allowed_domains = ['www.wal-martchina.com']
    start_urls = [
        'http://www.wal-martchina.com/walmart/store/2_beijing.htm',
        'http://www.wal-martchina.com/walmart/store/25_shandong.htm',
        ''
    ]

    def parse(self, response):
        tables = response.xpath('//div[@class="maincontent"]/table')
        try:
            for i in range(len(tables)):
                table = tables[i]
                rows = table.xpath('tr')
                lastCity = ''
                for j in range(len(rows)):
                    if j > 0:
                        row = rows[j]
                        cells = row.xpath('td')
                        cellLen = len(cells)
                        item = WalmartItem()
                        delta = 0
                        if cellLen is 7:
                            lastCity = text(cells[0])
                            delta = 1
                        elif cellLen is 6:
                            delta = 0
                        if cellLen > 5:
                            item['city'] = lastCity
                            item['name'] = text(cells[0 + delta])
                            item['address'] = text(cells[1 + delta])
                            item['tel'] = text(cells[2 + delta])
                            item['openTime'] = text(cells[4 + delta])
                            item['isSanm'] = i is 1
                            yield item
        except Exception as e:
            print e
