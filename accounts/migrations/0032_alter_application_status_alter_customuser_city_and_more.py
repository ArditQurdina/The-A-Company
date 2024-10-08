# Generated by Django 4.0.6 on 2022-10-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_alter_userlanguages_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pennding', 'Pennding'), ('Read', 'Read')], default='Pennding', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Ausbildung', 'Ausbildung'), ('Internship', 'Internship'), ('Work And Travel', 'Work And Travel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userexperiece',
            name='Country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userexperiece',
            name='city_usExp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Low-Intermediate', 'Low-Intermediate'), ('Advanced', 'Advanced'), ('High-Intermediate', 'High-Intermediate'), ('N/A', 'N/A'), ('Basic', 'Basic')], max_length=255),
        ),
    ]
