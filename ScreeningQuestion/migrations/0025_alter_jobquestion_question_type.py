# Generated by Django 4.1.1 on 2023-04-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningQuestion', '0024_alter_jobquestion_question_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobquestion',
            name='question_type',
            field=models.CharField(blank=True, choices=[('Yes/No', 'Yes/No'), ('Numeric', 'Numeric')], max_length=100, null=True),
        ),
    ]
