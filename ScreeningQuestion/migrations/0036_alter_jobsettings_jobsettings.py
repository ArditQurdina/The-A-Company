# Generated by Django 4.0.6 on 2023-05-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningQuestion', '0035_alter_jobquestion_question_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsettings',
            name='jobSettings',
            field=models.CharField(choices=[('F', 'Filter out & send rejection letters to applicants who dont meet qualifications'), ('NF', 'Don’t filter out applicants. I will manually review each application sent to me')], max_length=500),
        ),
    ]
