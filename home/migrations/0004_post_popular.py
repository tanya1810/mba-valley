# Generated by Django 3.0.7 on 2020-09-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200922_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]
