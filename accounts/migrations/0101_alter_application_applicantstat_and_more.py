# Generated by Django 4.2.1 on 2023-05-26 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0100_alter_application_status_alter_jobs_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicantStat',
            field=models.CharField(blank=True, choices=[('Qualified', 'Qualified'), ('Not qualified', 'Not qualified')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('Pennding', 'Pennding')], default='Pennding', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 26, 13, 33, 20, 889937), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 26, 13, 33, 20, 889937), null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Work and Travel', 'Work and Travel'), ('Trainee', 'Trainee'), ('Ausbildung', 'Ausbildung'), ('Internship', 'Internship')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('Close', 'Close'), ('Open', 'Open')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('High-Intermediate', 'High-Intermediate'), ('Low-Intermediate', 'Low-Intermediate'), ('Advanced', 'Advanced'), ('N/A', 'N/A')], max_length=255),
        ),
    ]
