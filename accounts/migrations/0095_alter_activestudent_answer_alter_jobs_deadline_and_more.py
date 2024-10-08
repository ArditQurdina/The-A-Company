# Generated by Django 4.1.1 on 2023-04-03 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0094_alter_application_status_alter_jobs_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activestudent',
            name='answer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 3, 16, 38, 37, 40380), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='housing',
            field=models.CharField(choices=[('Not provided', 'Not provided'), ('Provided', 'Provided')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 3, 16, 38, 37, 40380), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Work and Travel', 'Work and Travel'), ('Trainee', 'Trainee'), ('Ausbildung', 'Ausbildung')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('Close', 'Close'), ('Open', 'Open')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='degree',
            field=models.CharField(choices=[('Master', 'Master’s Degree'), ('Bachelor', 'Bachelor’s Degree')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Low-Intermediate', 'Low-Intermediate'), ('High-Intermediate', 'High-Intermediate'), ('Basic', 'Basic'), ('N/A', 'N/A'), ('Advanced', 'Advanced')], max_length=255),
        ),
    ]
