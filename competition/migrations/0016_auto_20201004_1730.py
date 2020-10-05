# Generated by Django 3.0.7 on 2020-10-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0015_auto_20201003_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='organiser',
        ),
        migrations.AddField(
            model_name='competition',
            name='organiser_email',
            field=models.CharField(default='Enter Your Organiser Email', max_length=50),
        ),
        migrations.AddField(
            model_name='competition',
            name='organiser_name',
            field=models.CharField(default='Enter Your Organiser Name', max_length=50),
        ),
    ]
