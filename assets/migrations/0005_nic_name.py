# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20151023_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='nic',
            name='name',
            field=models.CharField(max_length=64, null=True, verbose_name='\u7f51\u5361\u540d', blank=True),
        ),
    ]
