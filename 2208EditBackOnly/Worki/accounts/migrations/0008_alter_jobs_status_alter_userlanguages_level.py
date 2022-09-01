# Generated by Django 4.0.6 on 2022-08-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_application_status_alter_jobs_country_j_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Close', 'Close')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Limited working proficiency', 'Limited working proficiency'), ('Elementary proficiency', 'Elementary proficiency'), ('Professional working proficiency', 'Professional working proficiency'), ('Native or bilingual proficiency', 'Native or bilingual proficiency'), ('Full professional proficiency', 'Full professional proficiency')], max_length=255),
        ),
    ]
