# Generated by Django 4.0.6 on 2023-01-26 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0079_alter_application_status_alter_jobs_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activestudent',
            name='answer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='ApplicantStat',
            field=models.CharField(blank=True, choices=[('Not qualified', 'Not qualified'), ('Qualified', 'Qualified')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 1, 26, 9, 32, 49, 705357), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='housing',
            field=models.CharField(choices=[('Provided', 'Provided'), ('Not provided', 'Not provided')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 1, 26, 9, 32, 49, 705401), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Work and Travel', 'Work and Travel'), ('Trainee', 'Trainee'), ('Internship', 'Internship'), ('Ausbildung', 'Ausbildung')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type_of_work',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Advanced', 'Advanced'), ('Low-Intermediate', 'Low-Intermediate'), ('N/A', 'N/A'), ('High-Intermediate', 'High-Intermediate')], max_length=255),
        ),
    ]
