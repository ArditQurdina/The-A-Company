# Generated by Django 4.2.1 on 2023-06-15 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0117_alter_activestudent_answer_alter_jobs_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='meetWithUs',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='meetWithUsLink',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pennding', 'Pennding'), ('Read', 'Read')], default='Pennding', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 15, 13, 15, 21, 747498), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='housing',
            field=models.CharField(choices=[('Provided', 'Provided'), ('Not provided', 'Not provided')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 15, 13, 15, 21, 747498), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Trainee', 'Trainee'), ('Internship', 'Internship'), ('Ausbildung', 'Ausbildung'), ('Work and Travel', 'Work and Travel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('Close', 'Close'), ('Open', 'Open')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Advanced', 'Advanced'), ('Low-Intermediate', 'Low-Intermediate'), ('High-Intermediate', 'High-Intermediate'), ('N/A', 'N/A'), ('Basic', 'Basic')], max_length=255),
        ),
    ]
