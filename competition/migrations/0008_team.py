# Generated by Django 3.0.7 on 2020-09-22 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competition', '0007_register_clg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=100)),
                ('contact_no', phone_field.models.PhoneField(help_text='Add country code before the contact no.', max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_event', to='competition.competition')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_leader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]