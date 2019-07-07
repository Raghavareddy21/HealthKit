# Generated by Django 2.2.3 on 2019-07-07 04:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HealthKit', '0005_doctorresponse_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalCamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfPeopleIll', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999)], verbose_name='Ill People')),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='HealthKit.UserDetails')),
            ],
        ),
    ]