# Generated by Django 4.0.6 on 2023-03-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningQuestion', '0021_alter_jobquestion_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobquestion',
            name='question_type',
            field=models.CharField(blank=True, choices=[('Yes/No', 'Yes/No'), ('Numeric', 'Numeric')], max_length=100, null=True),
        ),
    ]
