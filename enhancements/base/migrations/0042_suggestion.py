# Generated by Django 3.1 on 2020-09-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_delete_doom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', editable='false', max_length=200)),
                ('suggestion', models.TextField(editable='false  ', max_length=4999)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]