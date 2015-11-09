# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_eventlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlog',
            name='event_type',
            field=models.SmallIntegerField(verbose_name='\u4e8b\u4ef6\u7c7b\u578b', choices=[(1, '\u786c\u4ef6\u53d8\u66f4'), (2, '\u65b0\u589e\u914d\u4ef6'), (3, '\u8bbe\u5907\u4e0b\u7ebf'), (4, '\u8bbe\u5907\u4e0a\u7ebf'), (5, '\u5b9a\u671f\u7ef4\u62a4'), (6, '\u4e1a\u52a1\u4e0a\u7ebf\\\u66f4\u65b0\\\u53d8\u66f4'), (7, '\u5176\u5b83')]),
        ),
    ]
