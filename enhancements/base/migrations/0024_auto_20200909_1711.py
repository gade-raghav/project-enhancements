# Generated by Django 3.1 on 2020-09-09 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_auto_20200909_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='progress_precentage',
            new_name='progress_percentage',
        ),
    ]
