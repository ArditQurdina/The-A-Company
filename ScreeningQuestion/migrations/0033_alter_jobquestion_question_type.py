# Generated by Django 4.0.6 on 2023-05-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningQuestion', '0032_alter_jobsettings_jobsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobquestion',
            name='question_type',
            field=models.CharField(blank=True, choices=[('Yes/No', 'Yes/No'), ('Numeric', 'Numeric')], max_length=100, null=True),
        ),
    ]
