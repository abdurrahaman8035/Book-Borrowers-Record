# Generated by Django 2.2 on 2020-04-10 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0016_auto_20200409_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='images/user-circle.svg', null=True, upload_to='images/')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('staff_id', models.CharField(max_length=15, unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'staff',
                'ordering': ['registration_date'],
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='expiring_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 24, 11, 30, 32, 883561), null=True),
        ),
    ]