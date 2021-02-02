# Generated by Django 3.0.2 on 2021-02-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210125_1052'),
        ('exercice', '0010_exercice_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercice',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='category.Category'),
        ),
    ]
