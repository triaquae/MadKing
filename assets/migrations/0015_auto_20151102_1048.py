# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0014_auto_20150901_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='valid_begin_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='valid_end_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 10, 48, 30, 110956, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
