# Generated by Django 2.1.2 on 2018-11-03 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20181103_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinglistindi',
            old_name='visting_members',
            new_name='visiting_members',
        ),
    ]
