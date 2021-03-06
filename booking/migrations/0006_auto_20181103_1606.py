# Generated by Django 2.1.2 on 2018-11-03 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20181103_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinglistindi',
            name='date_visit',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 16, 6, 59, 538363)),
        ),
        migrations.AlterField(
            model_name='bookinglistindi',
            name='slots_present',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookinglistindi',
            name='visited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookinglistindi',
            name='visiting_members',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookinglistorga',
            name='date_visit',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 16, 6, 59, 539190)),
        ),
        migrations.AlterField(
            model_name='bookinglistorga',
            name='slots_present',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookinglistorga',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]
