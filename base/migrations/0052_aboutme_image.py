# Generated by Django 3.1 on 2020-09-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0051_auto_20200916_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
