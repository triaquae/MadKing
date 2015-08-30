# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_auto_20151027_0409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nic',
            old_name='ip_addr',
            new_name='ipaddress',
        ),
        migrations.RenameField(
            model_name='nic',
            old_name='mac',
            new_name='macaddress',
        ),
    ]
