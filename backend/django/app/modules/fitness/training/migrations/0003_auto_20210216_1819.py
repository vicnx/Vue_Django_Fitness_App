# Generated by Django 3.0.2 on 2021-02-16 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210212_1535'),
        ('training', '0002_training_exercices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='profiles.Profile'),
        ),
    ]
