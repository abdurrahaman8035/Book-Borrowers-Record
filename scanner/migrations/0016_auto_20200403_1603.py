# Generated by Django 2.2 on 2020-04-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0015_auto_20200403_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_days',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]