# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0020_auto_20151109_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='trade_time',
            new_name='trade_date',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='warranty',
        ),
        migrations.AddField(
            model_name='asset',
            name='expire_date',
            field=models.DateField(null=True, verbose_name='\u8fc7\u4fdd\u4fee\u671f', blank=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='capacity',
            field=models.IntegerField(verbose_name='\u5185\u5b58\u5927\u5c0f(MB)'),
        ),
    ]
