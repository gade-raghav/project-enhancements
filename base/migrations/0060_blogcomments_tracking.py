# Generated by Django 3.1 on 2020-09-25 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0059_blogcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomments',
            name='tracking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.blog'),
        ),
    ]