# Generated by Django 2.2 on 2020-04-12 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_auto_20200412_2224'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Edit_Overdue_Charges',
        ),
        migrations.AlterField(
            model_name='book',
            name='expiring_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 26, 22, 28, 56, 831577), null=True),
        ),
        migrations.AlterField(
            model_name='staff_book',
            name='expiring_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 26, 22, 28, 56, 831577), null=True),
        ),
    ]
