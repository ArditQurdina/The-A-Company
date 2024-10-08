# Generated by Django 4.0.6 on 2022-08-04 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_application_status_alter_jobs_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='apply_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('Pennding', 'Pennding')], default='Pennding', max_length=50),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Full professional proficiency', 'Full professional proficiency'), ('Limited working proficiency', 'Limited working proficiency'), ('Elementary proficiency', 'Elementary proficiency'), ('Native or bilingual proficiency', 'Native or bilingual proficiency'), ('Professional working proficiency', 'Professional working proficiency')], max_length=255),
        ),
    ]
