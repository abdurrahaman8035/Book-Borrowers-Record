# Generated by Django 2.2 on 2020-04-18 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0007_auto_20200413_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['expiring_date']},
        ),
        migrations.AlterModelOptions(
            name='staff_book',
            options={'ordering': ['expiring_date']},
        ),
        migrations.AlterField(
            model_name='book',
            name='expiring_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 2, 7, 5, 8, 33411), null=True),
        ),
        migrations.AlterField(
            model_name='staff_book',
            name='expiring_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 2, 7, 5, 8, 33411), null=True),
        ),
    ]
