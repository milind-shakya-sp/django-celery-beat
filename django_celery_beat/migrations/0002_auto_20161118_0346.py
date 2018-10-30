# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 03:46
from __future__ import absolute_import, unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_celery_beat.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarSchedule',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('event', models.CharField(
                    choices=[('dusk_nautical', 'dusk_nautical'),
                             ('dawn_astronomical', 'dawn_astronomical'),
                             ('dawn_nautical', 'dawn_nautical'),
                             ('dawn_civil', 'dawn_civil'),
                             ('sunset', 'sunset'),
                             ('solar_noon', 'solar_noon'),
                             ('dusk_astronomical', 'dusk_astronomical'),
                             ('sunrise', 'sunrise'),
                             ('dusk_civil', 'dusk_civil')],
                    max_length=24, verbose_name='event')),
                ('latitude', models.DecimalField(
                    decimal_places=6, max_digits=9, verbose_name='latitude')),
                ('longitude', models.DecimalField(
                    decimal_places=6, max_digits=9, verbose_name='latitude')),
            ],
            options={
                'ordering': ['event', 'latitude', 'longitude'],
                'verbose_name': 'solar',
                'verbose_name_plural': 'solars',
            },
        ),
        migrations.AddField(
            model_name='periodictask',
            name='solar',
            field=models.ForeignKey(
                blank=True, help_text='Use a solar schedule',
                null=True, on_delete=django.db.models.deletion.CASCADE,
                to='django_celery_beat.SolarSchedule', verbose_name='solar'),
        ),
    ]
    custom_operations = [
        migrations.AddIndex(
            model_name='periodictask',
            index=django_celery_beat.models.CeleryMySQLIndex(
                fields=['name'],
                name='django_cele_name_9c39ec_idx'
            )
        )
    ]

    operations = operations + custom_operations
