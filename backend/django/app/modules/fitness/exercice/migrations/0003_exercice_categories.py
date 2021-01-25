# Generated by Django 3.0.2 on 2021-01-25 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210125_1052'),
        ('exercice', '0002_auto_20210125_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercice',
            name='categories',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='categories', to='category.Category'),
        ),
    ]
