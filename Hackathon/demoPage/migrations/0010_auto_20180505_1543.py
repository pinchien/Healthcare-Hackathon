# Generated by Django 2.0.5 on 2018-05-05 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0009_auto_20180505_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='inputTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 5, 15, 43, 39, 652573)),
        ),
    ]
