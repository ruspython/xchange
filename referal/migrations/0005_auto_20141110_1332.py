# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referal', '0004_auto_20141110_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='picture',
            field=models.ImageField(blank=True, verbose_name='banner picture', upload_to='pictures'),
            preserve_default=True,
        ),
    ]
