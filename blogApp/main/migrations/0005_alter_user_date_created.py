# Generated by Django 5.0.1 on 2024-01-31 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_categories_alter_user_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 31, 22, 22, 10, 664644)),
        ),
    ]
