# Generated by Django 2.0.5 on 2018-05-05 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0021_auto_20180505_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdata',
            name='userType',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 20, 51, 17, 916221), null=True),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 20, 51, 17, 916221), null=True),
        ),
    ]
