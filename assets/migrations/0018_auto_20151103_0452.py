# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_auto_20151103_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='cpu_core_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='cpu_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='cpu_model',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='manufactory',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='model',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='os_distribution',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='os_release',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='os_type',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='ram_size',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='newassetapprovalzone',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='\u5df2\u6279\u51c6'),
        ),
        migrations.AlterField(
            model_name='newassetapprovalzone',
            name='approved_by',
            field=models.ForeignKey(verbose_name='\u6279\u51c6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='newassetapprovalzone',
            name='approved_date',
            field=models.DateTimeField(null=True, verbose_name='\u6279\u51c6\u65e5\u671f', blank=True),
        ),
        migrations.AlterField(
            model_name='newassetapprovalzone',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6c47\u62a5\u65e5\u671f'),
        ),
    ]
