# Generated by Django 2.2.6 on 2019-11-21 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191118_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
