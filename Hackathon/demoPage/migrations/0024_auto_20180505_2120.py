# Generated by Django 2.0.5 on 2018-05-05 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0023_auto_20180505_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 20, 7, 444113), null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 20, 7, 444113), null=True),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 21, 20, 7, 444113), null=True),
        ),
    ]
