# Generated by Django 4.0.1 on 2022-01-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='dives',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meet',
            name='hasResults',
            field=models.BooleanField(default=False),
        ),
    ]
