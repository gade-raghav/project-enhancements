# Generated by Django 3.1 on 2020-09-02 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_project_github'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='github',
            new_name='github_link',
        ),
    ]
