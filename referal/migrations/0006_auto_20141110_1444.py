# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referal', '0005_auto_20141110_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='clicks',
            new_name='points',
        ),
    ]
