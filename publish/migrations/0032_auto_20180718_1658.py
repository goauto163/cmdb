# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-18 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0031_auto_20180718_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publishapprovalhistory',
            options={'verbose_name': '\u53d1\u5e03\u5355\u5ba1\u6279\u8bb0\u5f55', 'verbose_name_plural': '\u53d1\u5e03\u5355\u5ba1\u6279\u8bb0\u5f55'},
        ),
        migrations.AlterField(
            model_name='publishapprovalhistory',
            name='approve_count',
            field=models.CharField(choices=[(b'1', '\u7b2c\u4e00\u6b21\u5ba1\u6279'), (b'2', '\u7b2c\u4e8c\u6b21\u5ba1\u6279')], default=b'1', max_length=32, verbose_name='\u5ba1\u6279\u6b21\u6570'),
        ),
    ]
