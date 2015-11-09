# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0019_newassetapprovalzone_asset_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newassetapprovalzone',
            options={'verbose_name': '\u65b0\u4e0a\u7ebf\u5f85\u6279\u51c6\u8d44\u4ea7', 'verbose_name_plural': '\u65b0\u4e0a\u7ebf\u5f85\u6279\u51c6\u8d44\u4ea7'},
        ),
        migrations.AlterField(
            model_name='nic',
            name='bonding',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
