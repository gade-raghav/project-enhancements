# Generated by Django 3.1 on 2020-09-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200902_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
