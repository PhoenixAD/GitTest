#coding: utf-8
#encoding:utf-8

from django.db import models

# Create your models here.
class ScrapyModel(models.Model):
    title=models.CharField(u'标题',max_length=200)
    link = models.CharField(u'链接',max_length=200)
    desc = models.TextField(u'描述')
    def __str__(self):
        return self.title
    class Meta:
         verbose_name =u'课程信息'
         verbose_name_plural =u'课程信息'
         #app_label= u'爬虫'
         #db_table='myscrapy_scrapymodel'
'''        
class TestScrapy(models.Model):
    text= models.CharField(max_length=255)
    author= models.CharField(max_length=255)

    class Meta:
        app_label = 'myscrapy'
        db_table = 'test_scrapy'
        '''