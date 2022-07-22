# Generated by Django 4.0.6 on 2022-07-20 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220715_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('Pennding', 'Pennding')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='postDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='level',
            field=models.CharField(choices=[('Limited working proficiency', 'Limited working proficiency'), ('Elementary proficiency', 'Elementary proficiency'), ('Full professional proficiency', 'Full professional proficiency'), ('Native or bilingual proficiency', 'Native or bilingual proficiency'), ('Professional working proficiency', 'Professional working proficiency')], max_length=255),
        ),
    ]
