# Generated by Django 2.2 on 2020-04-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0019_auto_20200404_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_days',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]