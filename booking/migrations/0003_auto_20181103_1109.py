# Generated by Django 2.1.2 on 2018-11-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20181103_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinglistindi',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bookinglistindi',
            name='pin_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='bookinglistorga',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bookinglistorga',
            name='pin_code',
            field=models.CharField(max_length=10),
        ),
    ]