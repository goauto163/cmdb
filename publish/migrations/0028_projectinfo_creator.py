# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-17 18:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publish', '0027_auto_20180717_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator_of_projectinfo', to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u8005'),
        ),
    ]
