# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exporters import JsonLinesItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder
from pymongo import MongoClient

class Test1Pipeline(object):

    #def  __init__(self,file,**kwargs):
    #    **kwargs='ensure_ascii=False'

    def process_item(self, item, spider):
        #line=json.dumps(dict(item), ensure_ascii=False,encoding='utf-8') + "\n"
        #self.file.write(line.decode('unicode_escape'))
        #self.file.write(line.decode('utf-8'))
        return item
        #return json.dumps(dict(item),ensure_ascii=False,encodeing='utf-8')
    def spider_opened(self, spider):
        self.exporter=JsonLinesItemExporter(file,'ensure_ascii=False')




class JsonLinesItemExporterExt(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file = file
        kwargs.setdefault('ensure_ascii', not self.encoding)
        self.encoder = ScrapyJSONEncoder(**kwargs)
        mongoclient=MongoClient("mongodb://10.10.10.91:27017")
        db=mongoclient.crawl
        self.collection=db['test1']

    def export_item(self,item):
        super(JsonLinesItemExporterExt,self).export_item(item)
        itemdict=dict(item)
        #print('export_item=',item)
        self.collection.insert_one(itemdict)

    '''
    def export_item(self,item):
        JsonLinesItemExporter.export_item(item)
        content=dict(item)
        #print('export_item=',item)
        self.collection.insert_one(content)
    '''

    def process_item(self,item,spider):
        content=dict(item)
        print('process_item,content=',content)
        self.collection.insert_one(content)
        return item

'''
class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('/tmp/feeds/items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False,encoding='utf-8') + "\n"
        self.file.write(line.decode('utf-8'))
        return item
'''
