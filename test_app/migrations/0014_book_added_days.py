# Generated by Django 2.2 on 2020-03-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0013_auto_20200318_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='added_days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
