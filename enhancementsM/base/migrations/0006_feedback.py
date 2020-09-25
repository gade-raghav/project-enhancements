# Generated by Django 3.1 on 2020-09-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200902_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(choices=[('Extremely useful', 'Extremely useful'), ('Somewhat useful', 'Somewhat useful'), ('Not useful', 'Not useful')], editable='false', max_length=100)),
                ('choice2', models.CharField(choices=[('Extremely useful', 'Extremely useful'), ('Somewhat useful', 'Somewhat useful'), ('Not useful', 'Not useful')], editable='false', max_length=100)),
                ('other', models.CharField(blank=True, editable='false', max_length=100)),
                ('feedback', models.TextField(editable='flase', max_length=5000)),
                ('email', models.CharField(default='', editable='false', max_length=200)),
                ('choice3', models.CharField(editable='false', max_length=4)),
                ('date_created', models.DateTimeField(auto_now_add=True, choices=[('yes', 'yes'), ('no', 'no')])),
            ],
        ),
    ]