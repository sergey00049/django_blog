# Generated by Django 2.2.6 on 2019-11-22 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191121_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preview',
        ),
    ]