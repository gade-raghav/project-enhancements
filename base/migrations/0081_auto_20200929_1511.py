# Generated by Django 3.1 on 2020-09-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0080_auto_20200929_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='converted',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
