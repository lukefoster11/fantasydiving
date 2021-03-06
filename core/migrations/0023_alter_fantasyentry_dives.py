# Generated by Django 4.0.1 on 2022-01-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_fantasyentry_dives'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fantasyentry',
            name='dives',
            field=models.ManyToManyField(limit_choices_to={'event': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')}, to='core.DiveInstance'),
        ),
    ]
