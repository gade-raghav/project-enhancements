# Generated by Django 3.1 on 2020-09-10 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_auto_20200910_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='progress_percentage',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='progress',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
