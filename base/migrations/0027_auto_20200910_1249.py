# Generated by Django 3.1 on 2020-09-10 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_auto_20200909_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='tracker_id',
            new_name='trackerid',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='progress_percentage',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='updated_at',
        ),
    ]
