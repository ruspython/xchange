# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referal', '0007_auto_20141120_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='clicker',
            field=models.ForeignKey(blank=True, to='referal.Referral'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banner',
            name='site_owner',
            field=models.ForeignKey(related_name='banner_site_owner', blank=True, to='referal.Referral'),
            preserve_default=True,
        ),
    ]
