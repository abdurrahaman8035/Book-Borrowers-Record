# Generated by Django 2.2 on 2020-04-09 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0015_auto_20200409_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='expiring_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 23, 13, 29, 28, 258202), null=True),
        ),
    ]