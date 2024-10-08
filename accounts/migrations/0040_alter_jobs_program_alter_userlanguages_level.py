# Generated by Django 4.0.6 on 2022-10-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_alter_jobs_program_alter_userlanguages_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Ausbildung', 'Ausbildung'), ('Work And Travel', 'Work And Travel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Low-Intermediate', 'Low-Intermediate'), ('Advanced', 'Advanced'), ('High-Intermediate', 'High-Intermediate'), ('N/A', 'N/A')], max_length=255),
        ),
    ]
