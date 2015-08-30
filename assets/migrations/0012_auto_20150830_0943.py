# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_auto_20150830_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufactory',
            old_name='name',
            new_name='manufactory',
        ),
    ]
