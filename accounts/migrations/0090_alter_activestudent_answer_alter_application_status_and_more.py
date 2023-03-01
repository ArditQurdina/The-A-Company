# Generated by Django 4.1.1 on 2023-03-01 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0089_alter_activestudent_answer_alter_jobs_deadline_and_more'),
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
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 1, 8, 49, 33, 380533), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 1, 8, 49, 33, 380533), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Trainee', 'Trainee'), ('Ausbildung', 'Ausbildung'), ('Work and Travel', 'Work and Travel')], max_length=50),
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
            field=models.CharField(choices=[('Advanced', 'Advanced'), ('N/A', 'N/A'), ('Basic', 'Basic'), ('High-Intermediate', 'High-Intermediate'), ('Low-Intermediate', 'Low-Intermediate')], max_length=255),
        ),
    ]
