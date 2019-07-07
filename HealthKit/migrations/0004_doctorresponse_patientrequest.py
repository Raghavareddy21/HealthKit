# Generated by Django 2.2.3 on 2019-07-06 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HealthKit', '0003_otherdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symtomps', models.CharField(max_length=300, verbose_name='Symtomps')),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor1', to='HealthKit.UserDetails')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient1', to='HealthKit.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Solution', models.CharField(max_length=300, verbose_name='Solutions')),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor2', to='HealthKit.UserDetails')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient2', to='HealthKit.UserDetails')),
            ],
        ),
    ]
