# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-18 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publish', '0030_remove_publishsheet_project_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishsheet',
            name='first_approver',
            field=models.ManyToManyField(related_name='publishsheet_first_level_approver', to=settings.AUTH_USER_MODEL, verbose_name='\u4e00\u7ea7\u5ba1\u6279\u4eba'),
        ),
        migrations.AddField(
            model_name='publishsheet',
            name='second_approver',
            field=models.ManyToManyField(related_name='publishsheet_second_level_approver', to=settings.AUTH_USER_MODEL, verbose_name='\u4e8c\u7ea7\u5ba1\u6279\u4eba'),
        ),
    ]
