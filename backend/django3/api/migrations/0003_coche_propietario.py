# Generated by Django 3.0.2 on 2021-01-22 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_coche'),
    ]

    operations = [
        migrations.AddField(
            model_name='coche',
            name='propietario',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Employee'),
        ),
    ]