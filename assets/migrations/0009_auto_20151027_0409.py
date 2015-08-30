# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_auto_20151026_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disk',
            old_name='size',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='size',
            new_name='capacity',
        ),
    ]
