# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_newassetapprovalzone'),
    ]

    operations = [
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='approved_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='approved_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 3, 4, 42, 47, 214634, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
