# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20151026_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='raid_type',
            field=models.CharField(max_length=512, null=True, verbose_name='raid\u7c7b\u578b', blank=True),
        ),
    ]
