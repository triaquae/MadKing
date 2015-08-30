# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20151023_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='cpu_core_count',
            field=models.SmallIntegerField(default=1, verbose_name='cpu\u6838\u6570'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cpu',
            name='cpu_count',
            field=models.SmallIntegerField(default=1, verbose_name='\u7269\u7406cpu\u4e2a\u6570'),
            preserve_default=False,
        ),
    ]
