# Generated by Django 3.1 on 2020-09-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0071_auto_20200928_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='user_device_information',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
