# Generated by Django 4.0.1 on 2022-01-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_fantasyentry_dives'),
    ]

    operations = [
        migrations.AddField(
            model_name='diveinstance',
            name='score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
