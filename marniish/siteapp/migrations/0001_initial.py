# Generated by Django 5.1.3 on 2024-11-29 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=150)),
                ('parent_url', models.URLField(max_length=30)),
                ('parent_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('trend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteapp.trend')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('year', models.IntegerField()),
                ('doi', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(blank=True, max_length=100)),
                ('trend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteapp.trend')),
            ],
        ),
    ]
