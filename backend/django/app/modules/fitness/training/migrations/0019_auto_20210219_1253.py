# Generated by Django 3.0.2 on 2021-02-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0018_auto_20210208_1032'),
        ('training', '0018_auto_20210219_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficulty',
            name='exercice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercicies', related_query_name='exercicies', to='exercice.Exercice'),
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', related_query_name='trainings', to='training.Training'),
        ),
        migrations.AlterField(
            model_name='training',
            name='difficulties',
            field=models.ManyToManyField(related_name='difficulties', related_query_name='difficulties', through='training.Difficulty', to='exercice.Exercice'),
        ),
    ]