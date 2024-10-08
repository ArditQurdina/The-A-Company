# Generated by Django 4.0.6 on 2023-05-29 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0101_alter_application_applicantstat_and_more'),
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
            field=models.CharField(choices=[('Pennding', 'Pennding'), ('Read', 'Read')], default='Pennding', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 29, 7, 8, 8, 339042), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 29, 7, 8, 8, 339074), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Work and Travel', 'Work and Travel'), ('Internship', 'Internship'), ('Trainee', 'Trainee'), ('Ausbildung', 'Ausbildung')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type_of_work',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='degree',
            field=models.CharField(choices=[('Bachelor', 'Bachelor’s Degree'), ('Master', 'Master’s Degree')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Low-Intermediate', 'Low-Intermediate'), ('Advanced', 'Advanced'), ('High-Intermediate', 'High-Intermediate'), ('Basic', 'Basic')], max_length=255),
        ),
    ]
