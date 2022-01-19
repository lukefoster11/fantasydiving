# Generated by Django 4.0.1 on 2022-01-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_entry_dives_diveinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='FantasyEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dive1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.diveinstance')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
            ],
        ),
    ]