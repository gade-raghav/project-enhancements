# Generated by Django 3.1 on 2020-09-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_examplemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
