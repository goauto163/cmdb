# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-12 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0013_publishsheet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishsheet',
            name='status',
            field=models.CharField(choices=[(b'1', '\u5ba1\u6279\u4e2d'), (b'2', '\u5ba1\u6279\u62d2\u7edd'), (b'3', '\u5ba1\u6279\u901a\u8fc7'), (b'4', '\u5b8c\u6210\u53d1\u5e03')], default=b'1', max_length=32, verbose_name='\u53d1\u5e03\u5355\u72b6\u6001'),
        ),
    ]
