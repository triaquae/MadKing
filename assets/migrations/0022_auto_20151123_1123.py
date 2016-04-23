# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0021_auto_20151110_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='memo',
            field=models.CharField(max_length=128, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
