# Generated by Django 2.0.5 on 2018-05-05 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0025_auto_20180505_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 36, 53, 166274), null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 36, 53, 166274), null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='userId',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 36, 53, 166274), null=True),
        ),
    ]
