# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import re

class PastaPipeline(object):
    pattern = re.compile(r" {2,}")
    def process_item(self, item, spider):
        if item.get("time"):
            return {
                key: self.pattern.sub(" ", item[key].strip()) if isinstance(item[key], str) else item[key]
                for key in item.keys()
            }
        else:
            raise DropItem("Missing time in %s" % item)
