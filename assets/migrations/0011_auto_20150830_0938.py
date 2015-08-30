# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20151027_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu',
            old_name='model',
            new_name='cpu_model',
        ),
        migrations.AlterField(
            model_name='disk',
            name='capacity',
            field=models.FloatField(verbose_name='\u78c1\u76d8\u5bb9\u91cfGB'),
        ),
    ]
