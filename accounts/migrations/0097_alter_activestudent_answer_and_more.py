# Generated by Django 4.0.6 on 2023-04-03 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0096_jobs_sharewith_alter_application_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activestudent',
            name='answer',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='ApplicantStat',
            field=models.CharField(blank=True, choices=[('Not qualified', 'Not qualified'), ('Qualified', 'Qualified')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('Pennding', 'Pennding')], default='Pennding', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 3, 8, 16, 32, 191754), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='housing',
            field=models.CharField(choices=[('Provided', 'Provided'), ('Not provided', 'Not provided')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 3, 8, 16, 32, 191802), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Ausbildung', 'Ausbildung'), ('Internship', 'Internship'), ('Trainee', 'Trainee'), ('Work and Travel', 'Work and Travel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type_of_work',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='degree',
            field=models.CharField(choices=[('Bachelor', 'Bachelor’s Degree'), ('Master', 'Master’s Degree')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('N/A', 'N/A'), ('High-Intermediate', 'High-Intermediate'), ('Basic', 'Basic'), ('Low-Intermediate', 'Low-Intermediate'), ('Advanced', 'Advanced')], max_length=255),
        ),
    ]
