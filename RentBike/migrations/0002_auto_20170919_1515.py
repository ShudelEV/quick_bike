# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentBike', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='workday_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='day',
        ),
        migrations.RemoveField(
            model_name='price',
            name='one_hour',
        ),
        migrations.RemoveField(
            model_name='price',
            name='three_hours',
        ),
        migrations.AddField(
            model_name='price',
            name='weekend_day',
            field=models.FloatField(default=0, verbose_name='price for a day (weekend)'),
        ),
        migrations.AddField(
            model_name='price',
            name='weekend_one_hour',
            field=models.FloatField(default=0, verbose_name='price for an hour (weekend)'),
        ),
        migrations.AddField(
            model_name='price',
            name='weekend_three_hours',
            field=models.FloatField(default=0, verbose_name='price for three hours (weekend)'),
        ),
        migrations.AddField(
            model_name='price',
            name='work_day',
            field=models.FloatField(default=0, verbose_name='price for a day (workday)'),
        ),
        migrations.AddField(
            model_name='price',
            name='workday_one_hour',
            field=models.FloatField(default=0, verbose_name='price for an hour (workday)'),
        ),
        migrations.AddField(
            model_name='price',
            name='workday_three_hours',
            field=models.FloatField(default=0, verbose_name='price for three hours (workday)'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='state',
            field=models.BooleanField(verbose_name='busy'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='type',
            field=models.CharField(choices=[('1', 'male'), ('2', 'female'), ('3', "children's")], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='price',
            name='week',
            field=models.FloatField(default=0, verbose_name='price for a week'),
        ),
    ]
