# Generated by Django 4.2.4 on 2023-10-19 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe', '0011_alter_subscription_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 19, 10, 40, 33, 728181)),
        ),
    ]
