# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0012_auto_20150830_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u4e8b\u4ef6\u540d\u79f0')),
                ('event_type', models.SmallIntegerField(max_length=64, verbose_name='\u4e8b\u4ef6\u7c7b\u578b', choices=[(1, '\u786c\u4ef6\u53d8\u66f4'), (2, '\u65b0\u589e\u914d\u4ef6'), (3, '\u8bbe\u5907\u4e0b\u7ebf'), (4, '\u8bbe\u5907\u4e0a\u7ebf'), (5, '\u5b9a\u671f\u7ef4\u62a4'), (6, '\u4e1a\u52a1\u4e0a\u7ebf\\\u66f4\u65b0\\\u53d8\u66f4'), (7, '\u5176\u5b83')])),
                ('component', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe5\xad\x90\xe9\xa1\xb9', blank=True)),
                ('detail', models.TextField(verbose_name='\u4e8b\u4ef6\u8be6\u60c5')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u4e8b\u4ef6\u65f6\u95f4')),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
                ('user', models.ForeignKey(verbose_name='\u4e8b\u4ef6\u6e90', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4e8b\u4ef6\u7eaa\u5f55',
                'verbose_name_plural': '\u4e8b\u4ef6\u7eaa\u5f55',
            },
        ),
    ]
