# Generated by Django 2.2.3 on 2019-07-06 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthKit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('username', models.CharField(max_length=25, verbose_name='username')),
                ('password', models.CharField(max_length=15, verbose_name='password')),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age')),
                ('aadharNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999)], verbose_name='Aadhar Number')),
                ('email', models.EmailField(max_length=60, verbose_name='Email Address')),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('phoneNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Phone Number')),
                ('languages', models.ManyToManyField(to='HealthKit.Language')),
            ],
        ),
    ]