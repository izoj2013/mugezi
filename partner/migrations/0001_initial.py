# Generated by Django 3.1.2 on 2022-02-15 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('job_function', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=128)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('partnership_type', models.CharField(choices=[('Collaboration', 'Collaborate with us'), ('Demo Request', 'Request for a demo'), ('Hire Us', 'Hire our services')], default=None, max_length=64)),
                ('project_status', models.CharField(choices=[('Start', 'start'), ('Starting', 'starting'), ('In Progress', 'in-progress'), ('Finishing', 'finishing'), ('Completed', 'completed'), ('Abandoned', 'abandoned'), ('Halted', 'halted'), ('Frozen', 'frozen')], default='Start', max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=64)),
                ('project_status', models.CharField(choices=[('Start', 'start'), ('Starting', 'starting'), ('In Progress', 'in-progress'), ('Finishing', 'finishing'), ('Completed', 'completed'), ('Abandoned', 'abandoned'), ('Halted', 'halted'), ('Frozen', 'frozen')], default='Start', max_length=64)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_state', models.DateField(default=datetime.datetime(2022, 8, 15, 14, 31, 5, 848951))),
                ('comment', models.TextField(max_length=324)),
            ],
        ),
    ]