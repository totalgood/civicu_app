# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-28 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0011_auto_20171126_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='label',
            field=models.ManyToManyField(blank=True, choices=[('Wolf', 'Wolf'), ('Fox', 'Fox'), ('Wolverine', 'Wolverine'), ('Rabbit', 'Rabbit')], through='labeler.ImageLabel', to='labeler.Label'),
        ),
        migrations.AlterField(
            model_name='label',
            name='label',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
    ]