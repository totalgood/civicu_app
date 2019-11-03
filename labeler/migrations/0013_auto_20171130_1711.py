# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0012_auto_20171127_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagelabel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imagelabel',
            name='label',
        ),
        migrations.RemoveField(
            model_name='imagelabel',
            name='user',
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Quick picture caption'),
        ),
        migrations.AlterField(
            model_name='image',
            name='label',
            field=models.ManyToManyField(choices=[(7, 'Bear'), (8, 'Bird'), (9, 'Bobcat'), (10, 'Cougar'), (11, 'Coyote'), (12, 'Deer'), (13, 'Elk'), (14, 'Fox'), (15, 'Frog'), (16, 'Human'), (17, 'Marten'), (18, 'Sign'), (19, 'Skunk'), (20, 'Small-animal'), (21, 'Snowshoe-hare'), (22, 'Weasel'), (23, 'Wolverine'), (24, 'Wolf')], to='labeler.Label'),
        ),
        migrations.DeleteModel(
            name='ImageLabel',
        ),
    ]