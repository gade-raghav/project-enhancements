# Generated by Django 3.1 on 2020-09-28 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0063_auto_20200928_0519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ['-updated_at']},
        ),
    ]
