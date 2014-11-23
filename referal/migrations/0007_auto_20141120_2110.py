# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referal', '0006_auto_20141110_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='owner',
            new_name='clicker',
        ),
        migrations.AddField(
            model_name='banner',
            name='site_owner',
            field=models.ForeignKey(default=None, to='referal.Referral', related_name='banner_site_owner'),
            preserve_default=False,
        ),
    ]
