# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20151023_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='memo',
            field=models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
