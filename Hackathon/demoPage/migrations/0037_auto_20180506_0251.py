# Generated by Django 2.0.5 on 2018-05-06 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0036_auto_20180506_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 2, 51, 12, 627048), null=True),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 2, 51, 12, 611448), null=True),
        ),
        migrations.AlterField(
            model_name='riskdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 2, 51, 12, 627048), null=True),
        ),
    ]
