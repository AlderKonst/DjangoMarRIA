# Generated by Django 5.1.3 on 2024-12-01 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('trend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteapp.trend')),
            ],
        ),
    ]