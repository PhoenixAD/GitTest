# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 02:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysinfo', '0002_testscrapy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScrapyModel',
        ),
        migrations.DeleteModel(
            name='TestScrapy',
        ),
    ]