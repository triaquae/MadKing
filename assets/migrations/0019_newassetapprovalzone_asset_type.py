# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0018_auto_20151103_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='asset_type',
            field=models.CharField(blank=True, max_length=64, null=True, choices=[(b'server', '\u670d\u52a1\u5668'), (b'switch', '\u4ea4\u6362\u673a'), (b'router', '\u8def\u7531\u5668'), (b'firewall', '\u9632\u706b\u5899'), (b'storage', '\u5b58\u50a8\u8bbe\u5907'), (b'NLB', 'NetScaler'), (b'wireless', '\u65e0\u7ebfAP'), (b'software', '\u8f6f\u4ef6\u8d44\u4ea7'), (b'others', '\u5176\u5b83\u7c7b')]),
        ),
    ]
