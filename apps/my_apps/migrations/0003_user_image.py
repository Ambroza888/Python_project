# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-28 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_apps', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
