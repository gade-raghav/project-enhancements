# Generated by Django 3.1 on 2020-09-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20200908_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Discarded', 'Discarded'), ('Completed', 'Completed')], default='Queued', max_length=20),
        ),
    ]
