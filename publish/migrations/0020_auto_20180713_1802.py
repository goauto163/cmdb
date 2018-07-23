# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-13 18:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publish', '0019_auto_20180713_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishApprovalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve_count', models.PositiveSmallIntegerField(default=1, verbose_name='\u5ba1\u6279\u6b21\u6570')),
                ('approve_status', models.CharField(choices=[(b'1', '\u901a\u8fc7'), (b'2', '\u62d2\u7edd')], default=b'1', max_length=32, verbose_name='\u5ba1\u6279\u72b6\u6001')),
                ('first_approve_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u7b2c\u4e00\u5ba1\u6279\u65f6\u95f4')),
                ('first_notices', models.TextField(blank=True, null=True, verbose_name='\u7b2c\u4e00\u5ba1\u6279\u4eba\u6279\u6ce8\u7684\u6ce8\u610f\u4e8b\u9879')),
                ('second_approve_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u7b2c\u4e8c\u5ba1\u6279\u65f6\u95f4')),
                ('second_notices', models.TextField(blank=True, null=True, verbose_name='\u7b2c\u4e8c\u5ba1\u6279\u4eba\u6279\u6ce8\u7684\u6ce8\u610f\u4e8b\u9879')),
                ('refuse_reason', models.TextField(blank=True, null=True, verbose_name='\u62d2\u7edd\u539f\u56e0')),
                ('first_approver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sheet_first_approver', to=settings.AUTH_USER_MODEL, verbose_name='\u7b2c\u4e00\u5ba1\u6279\u4eba')),
            ],
            options={
                'verbose_name': '\u53d1\u5e03\u5355\u5ba1\u6279\u5386\u53f2',
                'verbose_name_plural': '\u53d1\u5e03\u5355\u5ba1\u6279\u5386\u53f2',
            },
        ),
        migrations.RemoveField(
            model_name='publishsheet',
            name='refuse_reason',
        ),
        migrations.AlterField(
            model_name='publishsheet',
            name='status',
            field=models.CharField(choices=[(b'1', '\u5ba1\u6279\u4e2d'), (b'2', '\u5ba1\u6279\u62d2\u7edd'), (b'3', '\u5ba1\u6279\u901a\u8fc7'), (b'4', '\u5b8c\u6210\u53d1\u5e03'), (b'5', '\u867d\u5ba1\u6279\u901a\u8fc7\uff0c\u4f46\u8d85\u65f6\u672a\u53d1\u5e03')], default=b'1', max_length=32, verbose_name='\u53d1\u5e03\u5355\u72b6\u6001'),
        ),
        migrations.AddField(
            model_name='publishapprovalhistory',
            name='publish_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.PublishSheet'),
        ),
        migrations.AddField(
            model_name='publishapprovalhistory',
            name='second_approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sheet_second_approver', to=settings.AUTH_USER_MODEL, verbose_name='\u7b2c\u4e8c\u5ba1\u6279\u4eba'),
        ),
    ]
