# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_nic_bonding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nic',
            name='model',
            field=models.CharField(max_length=128, null=True, verbose_name='\u7f51\u5361\u578b\u53f7', blank=True),
        ),
    ]
