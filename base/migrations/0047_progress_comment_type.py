# Generated by Django 3.1 on 2020-09-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_remove_progress_progress_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='comment_type',
            field=models.CharField(choices=[('Suggestion', 'Suggestion'), ('Task', 'Task')], default='Suggestion', max_length=20, null=True),
        ),
    ]
