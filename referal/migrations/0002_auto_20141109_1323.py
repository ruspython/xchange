# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('referal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('url', models.URLField()),
                ('picture', django_resized.forms.ResizedImageField(upload_to='banners/pictures')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('site_url', models.URLField()),
                ('clicks', models.BigIntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='referal',
            name='user',
        ),
        migrations.DeleteModel(
            name='Referal',
        ),
        migrations.AddField(
            model_name='banner',
            name='owner',
            field=models.ForeignKey(to='referal.Referral'),
            preserve_default=True,
        ),
    ]
