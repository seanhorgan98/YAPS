# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('YAPS', '0002_auto_20180320_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YAPS.Category')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='audio_file',
            field=models.FileField(default='', upload_to='episode'),
        ),
        migrations.AddField(
            model_name='episode',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='audio_file',
            field=models.FileField(default='', upload_to='episode'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YAPS.Category'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]