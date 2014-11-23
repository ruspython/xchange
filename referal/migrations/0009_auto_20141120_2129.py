# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referal', '0008_auto_20141120_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='clicker',
            new_name='banner_owner',
        ),
    ]
