# encoding: utf-8
#-*-coding:utf-8-*-
'''
Created on 2017年7月17日

@author: David
'''

def setup_django_env():
    import os, django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")
    django.setup()

def check_db_connection():
    from django.db import connection

    if connection.connection:
        #NOTE: (zacky, 2016.MAR.21st) IF CONNECTION IS CLOSED BY BACKEND, CLOSE IT AT DJANGO, WHICH WILL BE SETUP AFTERWARDS.
        if not connection.is_usable():
            connection.close()
