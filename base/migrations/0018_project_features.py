# Generated by Django 3.1 on 2020-09-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20200907_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='features',
            field=models.BooleanField(default=False),
        ),
    ]
