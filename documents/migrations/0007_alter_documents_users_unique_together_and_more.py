# Generated by Django 4.0.6 on 2023-05-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_recruiterdocument_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='documents_users',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='recruiterdocument',
            name='status',
        ),
        migrations.AddField(
            model_name='documents_users',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Refused')], default='P', max_length=100),
        ),
        migrations.AddField(
            model_name='recruiterdocument',
            name='signed',
            field=models.BooleanField(default=False),
        ),
    ]
