# Generated by Django 3.1.2 on 2022-02-15 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('donor_type', models.CharField(choices=[('Individual Donor', 'individual-donor'), ('Group Donorr', 'group-donor')], default='Individual Donor', max_length=64)),
                ('organisation_name', models.CharField(max_length=64)),
                ('pledge_amount', models.FloatField()),
                ('pledge_date', models.DateField(auto_now_add=True)),
                ('pledge_status', models.CharField(choices=[('Not-Honoured Pledge', 'not-honoured-pledge'), ('Honoured Pledge', 'honoured-pledge')], default='Not-Honoured Pledge', max_length=64)),
                ('received_amount', models.FloatField(default=0.0)),
                ('receipt_date', models.DateTimeField(default=datetime.datetime(2022, 5, 15, 14, 31, 5, 847672))),
            ],
        ),
    ]