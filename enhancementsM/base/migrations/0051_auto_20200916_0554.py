# Generated by Django 3.1 on 2020-09-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0050_progress_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='task_completed',
            field=models.BooleanField(blank=True),
        ),
    ]
