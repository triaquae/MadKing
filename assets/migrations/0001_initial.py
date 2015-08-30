# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u5b57')),
                ('token', models.CharField(default=None, max_length=128, null=True, verbose_name='token', blank=True)),
                ('department', models.CharField(default=None, max_length=32, null=True, verbose_name='\u90e8\u95e8', blank=True)),
                ('tel', models.CharField(default=None, max_length=32, null=True, verbose_name='\u5ea7\u673a', blank=True)),
                ('mobile', models.CharField(default=None, max_length=32, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('memo', models.TextField(default=None, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_type', models.CharField(default=b'server', max_length=64, choices=[(b'server', '\u670d\u52a1\u5668'), (b'switch', '\u4ea4\u6362\u673a'), (b'router', '\u8def\u7531\u5668'), (b'firewall', '\u9632\u706b\u5899'), (b'storage', '\u5b58\u50a8\u8bbe\u5907'), (b'NLB', 'NetScaler'), (b'wireless', '\u65e0\u7ebfAP'), (b'software', '\u8f6f\u4ef6\u8d44\u4ea7'), (b'others', '\u5176\u5b83\u7c7b')])),
                ('name', models.CharField(unique=True, max_length=64)),
                ('sn', models.CharField(unique=True, max_length=128, verbose_name='\u8d44\u4ea7SN\u53f7')),
                ('management_ip', models.GenericIPAddressField(null=True, verbose_name='\u7ba1\u7406IP', blank=True)),
                ('trade_time', models.DateField(null=True, verbose_name='\u8d2d\u4e70\u65f6\u95f4', blank=True)),
                ('warranty', models.SmallIntegerField(null=True, verbose_name='\u4fdd\u4fee\u671f', blank=True)),
                ('price', models.FloatField(null=True, verbose_name='\u4ef7\u683c', blank=True)),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(verbose_name='\u8d44\u4ea7\u7ba1\u7406\u5458', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
                'verbose_name_plural': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u4e1a\u52a1\u7ebf')),
                ('memo', models.CharField(max_length=64, verbose_name='\u5907\u6ce8', blank=True)),
                ('parent_unit', models.ForeignKey(related_name='parent_level', blank=True, to='assets.BusinessUnit', null=True)),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=128, verbose_name='\u5408\u540c\u53f7')),
                ('name', models.CharField(max_length=64, verbose_name='\u5408\u540c\u540d\u79f0')),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('price', models.IntegerField(verbose_name='\u5408\u540c\u91d1\u989d')),
                ('detail', models.TextField(null=True, verbose_name='\u5408\u540c\u8be6\u7ec6', blank=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('license_num', models.IntegerField(verbose_name='license\u6570\u91cf', blank=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u5408\u540c',
                'verbose_name_plural': '\u5408\u540c',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=128, verbose_name='CPU\u578b\u53f7', blank=True)),
                ('cpu_count', models.SmallIntegerField(verbose_name='\u7269\u7406cpu\u4e2a\u6570')),
                ('cpu_core_count', models.SmallIntegerField(verbose_name='cpu\u6838\u6570')),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.OneToOneField(to='assets.Asset')),
            ],
            options={
                'verbose_name': 'CPU\u90e8\u4ef6',
                'verbose_name_plural': 'CPU\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, null=True, verbose_name='SN\u53f7', blank=True)),
                ('slot', models.CharField(max_length=64, verbose_name='\u63d2\u69fd\u4f4d')),
                ('manufactory', models.CharField(max_length=64, null=True, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\u78c1\u76d8\u578b\u53f7', blank=True)),
                ('size', models.FloatField(verbose_name='\u78c1\u76d8\u5bb9\u91cfkb')),
                ('iface_type', models.CharField(default=b'SAS', max_length=64, verbose_name='\u63a5\u53e3\u7c7b\u578b', choices=[(b'SATA', b'SATA'), (b'SAS', b'SAS'), (b'SCSI', b'SCSI'), (b'SSD', b'SSD')])),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
            options={
                'verbose_name': '\u786c\u76d8',
                'verbose_name_plural': '\u786c\u76d8',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('memo', models.CharField(max_length=128, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u5382\u5546\u540d\u79f0')),
                ('support_num', models.CharField(max_length=30, verbose_name='\u652f\u6301\u7535\u8bdd', blank=True)),
                ('memo', models.CharField(max_length=128, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u5382\u5546',
                'verbose_name_plural': '\u5382\u5546',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vlan_ip', models.GenericIPAddressField(null=True, verbose_name='VlanIP', blank=True)),
                ('intranet_ip', models.GenericIPAddressField(null=True, verbose_name='\u5185\u7f51IP', blank=True)),
                ('sn', models.CharField(unique=True, max_length=128, verbose_name='SN\u53f7')),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\u578b\u53f7', blank=True)),
                ('port_num', models.SmallIntegerField(null=True, verbose_name='\u7aef\u53e3\u4e2a\u6570', blank=True)),
                ('device_detail', models.TextField(null=True, verbose_name='\u8bbe\u7f6e\u8be6\u7ec6\u914d\u7f6e', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.OneToOneField(to='assets.Asset')),
            ],
            options={
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907',
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, null=True, verbose_name='SN\u53f7', blank=True)),
                ('model', models.CharField(max_length=128, verbose_name='\u7f51\u5361\u578b\u53f7')),
                ('mac', models.CharField(unique=True, max_length=64, verbose_name='MAC')),
                ('ip_addr', models.GenericIPAddressField(null=True, verbose_name='IP', blank=True)),
                ('netmask', models.CharField(max_length=64, null=True, blank=True)),
                ('memo', models.CharField(max_length=128, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
            options={
                'verbose_name': '\u7f51\u5361',
                'verbose_name_plural': '\u7f51\u5361',
            },
        ),
        migrations.CreateModel(
            name='RaidAdaptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, null=True, verbose_name='SN\u53f7', blank=True)),
                ('slot', models.CharField(max_length=64, verbose_name='\u63d2\u53e3')),
                ('model', models.CharField(max_length=64, null=True, verbose_name='\u578b\u53f7', blank=True)),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, null=True, verbose_name='SN\u53f7', blank=True)),
                ('model', models.CharField(max_length=128, verbose_name='\u5185\u5b58\u578b\u53f7')),
                ('slot', models.CharField(max_length=64, verbose_name='\u63d2\u69fd')),
                ('size', models.IntegerField(verbose_name='\u5185\u5b58\u5927\u5c0f(KB)')),
                ('memo', models.CharField(max_length=128, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.ForeignKey(to='assets.Asset')),
            ],
            options={
                'verbose_name': 'RAM',
                'verbose_name_plural': 'RAM',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_by', models.CharField(default=b'auto', max_length=32, choices=[(b'auto', b'Auto'), (b'manual', b'Manual')])),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\u578b\u53f7', blank=True)),
                ('raid_type', models.TextField(null=True, verbose_name='raid\u7c7b\u578b', blank=True)),
                ('os_type', models.CharField(max_length=64, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7c7b\u578b', blank=True)),
                ('os_distribution', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u578b\u7248\u672c', blank=True)),
                ('os_release', models.CharField(max_length=64, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(null=True, blank=True)),
                ('asset', models.OneToOneField(to='assets.Asset')),
                ('hosted_on', models.ForeignKey(related_name='hosted_on_server', blank=True, to='assets.Server', null=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=1, help_text='eg. GNU/Linux', max_length=64, verbose_name='\u7cfb\u7edf\u7c7b\u578b', choices=[(b'linux', b'Linux'), (b'windows', b'Windows'), (b'network_firmware', b'Network Firmware'), (b'software', b'Softwares')])),
                ('distribution', models.CharField(default=b'windows', max_length=32, verbose_name='\u53d1\u578b\u7248\u672c', choices=[(b'windows', b'Windows'), (b'centos', b'CentOS'), (b'ubuntu', b'Ubuntu')])),
                ('version', models.CharField(help_text='eg. CentOS release 6.5 (Final)', unique=True, max_length=64, verbose_name='\u8f6f\u4ef6/\u7cfb\u7edf\u7248\u672c')),
                ('language', models.CharField(default=b'cn', max_length=32, verbose_name='\u7cfb\u7edf\u8bed\u8a00', choices=[(b'cn', '\u4e2d\u6587'), (b'en', '\u82f1\u6587')])),
            ],
            options={
                'verbose_name': '\u8f6f\u4ef6/\u7cfb\u7edf',
                'verbose_name_plural': '\u8f6f\u4ef6/\u7cfb\u7edf',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'Tag name')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('creater', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='firmware',
            field=models.ForeignKey(blank=True, to='assets.Software', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u4e1a\u52a1\u7ebf', blank=True, to='assets.BusinessUnit', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(verbose_name='\u5408\u540c', blank=True, to='assets.Contract', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(verbose_name='IDC\u673a\u623f', blank=True, to='assets.IDC', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufactory',
            field=models.ForeignKey(verbose_name='\u5236\u9020\u5546', blank=True, to='assets.Manufactory', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='tags',
            field=models.ManyToManyField(to='assets.Tag', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='ram',
            unique_together=set([('asset', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='raidadaptor',
            unique_together=set([('asset', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='disk',
            unique_together=set([('asset', 'slot')]),
        ),
    ]
