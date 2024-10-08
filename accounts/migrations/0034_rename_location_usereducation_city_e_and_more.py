# Generated by Django 4.0.6 on 2022-10-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_usereducation_location_alter_jobs_program_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usereducation',
            old_name='location',
            new_name='city_e',
        ),
        migrations.AddField(
            model_name='usereducation',
            name='country_e',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('Pennding', 'Pennding')], default='Pennding', max_length=50),
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
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('High-Intermediate', 'High-Intermediate'), ('Low-Intermediate', 'Low-Intermediate'), ('Advanced', 'Advanced'), ('N/A', 'N/A')], max_length=255),
        ),
    ]
