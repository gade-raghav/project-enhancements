# Generated by Django 3.1 on 2020-09-28 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0073_bug_ticket_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('comment', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('tracking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.bug')),
            ],
        ),
    ]
