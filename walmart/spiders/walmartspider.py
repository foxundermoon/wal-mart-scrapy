# -*- coding: utf-8 -*-
import scrapy
from walmart.items import WalmartItem


def text(elt):
    txt = elt.xpath('string(.)')[0].root
    return txt.replace('\n', '  ').encode('utf-8')


class WalmartSpider(scrapy.Spider):
    name = 'walmart'
    allowed_domains = ['www.wal-martchina.com']
    start_urls = [
        'http://www.wal-martchina.com/walmart/store/10_hebei.htm',
        'http://www.wal-martchina.com/walmart/store/11_heilongjiang.htm',
        'http://www.wal-martchina.com/walmart/store/12_henan.htm',
        'http://www.wal-martchina.com/walmart/store/14_hubei.htm',
        'http://www.wal-martchina.com/walmart/store/15_hunan.htm',
        'http://www.wal-martchina.com/walmart/store/16_innermongolia.htm',
        'http://www.wal-martchina.com/walmart/store/17_jiangsu.htm',
        'http://www.wal-martchina.com/walmart/store/18_jiangxi.htm',
        'http://www.wal-martchina.com/walmart/store/19_jilin.htm',
        'http://www.wal-martchina.com/walmart/store/1_anhui.htm',
        'http://www.wal-martchina.com/walmart/store/20_liaoning.htm',
        'http://www.wal-martchina.com/walmart/store/24_shaanxi.htm',
        'http://www.wal-martchina.com/walmart/store/25_shandong.htm',
        'http://www.wal-martchina.com/walmart/store/26_shanghai.htm',
        'http://www.wal-martchina.com/walmart/store/27_shanxi.htm',
        'http://www.wal-martchina.com/walmart/store/28_sichuan.htm',
        'http://www.wal-martchina.com/walmart/store/2_beijing.htm',
        'http://www.wal-martchina.com/walmart/store/31_tianjin.htm',
        'http://www.wal-martchina.com/walmart/store/33_yunnan.htm',
        'http://www.wal-martchina.com/walmart/store/34_zhejiang.htm',
        'http://www.wal-martchina.com/walmart/store/3_chongqing.htm',
        'http://www.wal-martchina.com/walmart/store/4_fujian.htm',
        'http://www.wal-martchina.com/walmart/store/6_guangdong.htm',
        'http://www.wal-martchina.com/walmart/store/7_guangxi.htm',
        'http://www.wal-martchina.com/walmart/store/8_guizhou.htm',
    ]

    def parse(self, response):
        tables = response.xpath('//div[@class="maincontent"]/table')
        area = response.xpath('//div[@class="maincontent"]/p[@class="style2"]')
        areaStr = text(area)
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
                            item['area'] = areaStr
                            item['city'] = lastCity
                            item['name'] = text(cells[0 + delta])
                            item['address'] = text(cells[1 + delta])
                            item['tel'] = text(cells[2 + delta])
                            item['openTime'] = text(cells[4 + delta])
                            item['isSanm'] = i is 1
                            yield item
        except Exception as e:
            print e
