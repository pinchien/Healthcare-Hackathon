# Generated by Django 2.0.5 on 2018-05-05 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0003_auto_20180504_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='inputTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 5, 15, 10, 29, 857718)),
        ),
    ]
