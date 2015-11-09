# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_auto_20151102_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewAssetApprovalZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=128, verbose_name='\u8d44\u4ea7SN\u53f7')),
                ('data', models.TextField(verbose_name='\u8d44\u4ea7\u6570\u636e')),
            ],
        ),
    ]
