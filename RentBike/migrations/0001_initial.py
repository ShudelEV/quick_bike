# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.URLField()),
                ('type', models.CharField(choices=[('1', 'male'), ('2', 'female'), ('3', "children's")], max_length=1)),
                ('state', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.URLField(verbose_name='company photo')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_from', models.DateTimeField(verbose_name='from')),
                ('time_to', models.DateTimeField(verbose_name='to')),
                ('invoice', models.FloatField()),
                ('accessories', models.ManyToManyField(to='RentBike.Accessory')),
                ('bikes', models.ManyToManyField(to='RentBike.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_hour', models.FloatField(verbose_name='price for an hour')),
                ('three_hours', models.FloatField(verbose_name='price for three hours')),
                ('day', models.FloatField(verbose_name='price for a day')),
                ('week', models.FloatField(verbose_name='price for a week')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.ContactInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.URLField(verbose_name='shop photo')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.Company')),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.ContactInfo')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.Profile'),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.ContactInfo'),
        ),
        migrations.AddField(
            model_name='bike',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.Shop'),
        ),
        migrations.AddField(
            model_name='bike',
            name='workday_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.Price'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.Price'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentBike.Shop'),
        ),
    ]