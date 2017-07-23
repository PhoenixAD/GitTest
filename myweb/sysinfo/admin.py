from django.contrib import admin
from .models import Message
import sys
sys.path.append("/myweb/myscrapy")
from myscrapy.models import ScrapyModel
#from 'D:\sorcecode\eclipse\django\myweb\myscrapy\models.py' import TestScrapy,ScrapyModel

# Register your models here.

#admin.site.register(Message)

class MessageAdmin(admin.ModelAdmin):
    list_display=('name','title','content','email','pub_date')
    search_fields=('name',)
    list_filter=('pub_date',)
    fields = ('name', 'title', 'content','email')
    #filter_horizontal = ('name',) �ֶα����Զ�
    #raw_id_fields = ('name',)  �ֶα��������
admin.site.register(Message,MessageAdmin)
#admin.site.register(TestScrapy)
admin.site.register(ScrapyModel)
