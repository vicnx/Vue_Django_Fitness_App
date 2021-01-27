# Generated by Django 2.1.1 on 2018-09-17 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professionalInformation', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('RG', models.CharField(max_length=11, unique=True)),
                ('CPF', models.CharField(max_length=13, unique=True)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('dateOfBirth', models.DateField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('professionalInformation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='professionalInformation.ProfessionalInformation')),
            ],
        ),
    ]