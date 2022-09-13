# Generated by Django 4.0.6 on 2022-09-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_application_status_alter_customuser_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='program',
            field=models.CharField(choices=[('Work And Travel', 'Work And Travel'), ('Ausbildung', 'Ausbildung'), ('Internship', 'Internship')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Native or bilingual proficiency', 'Native or bilingual proficiency'), ('Limited working proficiency', 'Limited working proficiency'), ('Full professional proficiency', 'Full professional proficiency'), ('Elementary proficiency', 'Elementary proficiency'), ('Professional working proficiency', 'Professional working proficiency')], max_length=255),
        ),
    ]
