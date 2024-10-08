# Generated by Django 4.2.1 on 2023-06-05 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0114_alter_application_applicantstat_alter_jobs_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activestudent',
            name='answer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pennding', 'Pennding'), ('Read', 'Read')], default='Pennding', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 5, 14, 36, 48, 403343), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='housing',
            field=models.CharField(choices=[('Not provided', 'Not provided'), ('Provided', 'Provided')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 5, 14, 36, 48, 403343), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Trainee', 'Trainee'), ('Internship', 'Internship'), ('Work and Travel', 'Work and Travel'), ('Ausbildung', 'Ausbildung')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Close', 'Close')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type_of_work',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='degree',
            field=models.CharField(choices=[('Master', 'Master’s Degree'), ('Bachelor', 'Bachelor’s Degree')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('High-Intermediate', 'High-Intermediate'), ('Advanced', 'Advanced'), ('N/A', 'N/A'), ('Low-Intermediate', 'Low-Intermediate'), ('Basic', 'Basic')], max_length=255),
        ),
    ]
