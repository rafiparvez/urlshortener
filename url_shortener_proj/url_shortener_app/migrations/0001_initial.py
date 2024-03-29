# Generated by Django 3.1 on 2020-08-22 12:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('hashed_url', models.URLField(unique=True)),
                ('num_url_clicks', models.IntegerField(default=0)),
                ('url_clicked_at', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(blank=True), default=list, size=None)),
                ('url_click_client', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='127.0.0.1', max_length=100), default=list, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
