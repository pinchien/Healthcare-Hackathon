# Generated by Django 2.0.5 on 2018-05-05 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0022_auto_20180505_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(blank=True, max_length=10, null=True)),
                ('cardioMin', models.CharField(blank=True, max_length=10, null=True)),
                ('sportsMin', models.CharField(blank=True, max_length=3, null=True)),
                ('strengthMin', models.CharField(blank=True, max_length=10, null=True)),
                ('weightMin', models.CharField(blank=True, max_length=10, null=True)),
                ('breakfastkCal', models.CharField(blank=True, max_length=10, null=True)),
                ('breakfastProtein', models.CharField(blank=True, max_length=10, null=True)),
                ('breakfastCarb', models.CharField(blank=True, max_length=10, null=True)),
                ('breakfastFat', models.CharField(blank=True, max_length=10, null=True)),
                ('lunchkCal', models.CharField(blank=True, max_length=10, null=True)),
                ('lunchProtein', models.CharField(blank=True, max_length=10, null=True)),
                ('lunchCarb', models.CharField(blank=True, max_length=10, null=True)),
                ('lunchFat', models.CharField(blank=True, max_length=10, null=True)),
                ('dinnerkCal', models.CharField(blank=True, max_length=10, null=True)),
                ('dinnerProtein', models.CharField(blank=True, max_length=10, null=True)),
                ('dinnerCarb', models.CharField(blank=True, max_length=10, null=True)),
                ('dinnerFat', models.CharField(blank=True, max_length=10, null=True)),
                ('inputTime', models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 15, 21, 20281), null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 15, 21, 20281), null=True),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 15, 21, 20281), null=True),
        ),
    ]
