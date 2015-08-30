# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='cpu_core_count',
        ),
        migrations.RemoveField(
            model_name='cpu',
            name='cpu_count',
        ),
    ]
