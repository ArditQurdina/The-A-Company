# Generated by Django 4.2.4 on 2023-10-23 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe', '0014_alter_subscription_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 23, 10, 21, 53, 805059)),
        ),
    ]
