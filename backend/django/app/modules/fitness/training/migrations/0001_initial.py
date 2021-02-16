# Generated by Django 3.0.2 on 2021-02-16 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0005_auto_20210212_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, default='https://upload.wikimedia.org/wikipedia/commons/8/84/Musculation_exercice_abdominal.png', max_length=255, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training', to='profiles.Profile')),
            ],
        ),
    ]