# Generated by Django 3.1 on 2020-10-16 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0086_project_project_bug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_bug',
            new_name='project_bugs',
        ),
    ]
