# Generated by Django 4.0.1 on 2022-01-15 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='entriesPath',
        ),
        migrations.RemoveField(
            model_name='meet',
            name='path',
        ),
    ]
