# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-24 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0005_auto_20180224_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='gallery',
            field=models.ManyToManyField(to='photologue.Gallery'),
        ),
    ]
