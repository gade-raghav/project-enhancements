# Generated by Django 3.1 on 2020-09-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20200903_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='choice1',
            field=models.CharField(blank='True', choices=[('Extremely useful', 'Extremely useful'), ('Somewhat useful', 'Somewhat useful'), ('Not useful', 'Not useful')], default='Extremely useful', editable='false', max_length=100),
        ),
    ]