# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import datetime
file=open('walmart_{}.csv'.format(datetime.datetime.now()), 'wb')
fieldnames=['city','name','address','tel','openTime','isSanm']
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()
class WalmartPipeline(object):
    def process_item(self, item, spider):
        row=dict(item)
        writer.writerow(row)
        return item
