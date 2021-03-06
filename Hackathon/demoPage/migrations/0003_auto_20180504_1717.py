# Generated by Django 2.0.5 on 2018-05-04 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demoPage', '0002_remove_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('age', models.CharField(max_length=3)),
                ('edu_level', models.CharField(max_length=2)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('inputTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
