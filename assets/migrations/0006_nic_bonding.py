# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_nic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='nic',
            name='bonding',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
