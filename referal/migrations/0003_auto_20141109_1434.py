# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referal', '0002_auto_20141109_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='picture',
            field=models.ImageField(upload_to='banners/pictures'),
            preserve_default=True,
        ),
    ]
