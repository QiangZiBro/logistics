# Generated by Django 2.1.7 on 2019-04-03 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logsapp', '0012_auto_20190404_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='good_name',
            new_name='package_name',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='good_type',
            new_name='package_type',
        ),
    ]