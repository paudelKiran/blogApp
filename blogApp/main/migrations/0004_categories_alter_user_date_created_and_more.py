# Generated by Django 5.0.1 on 2024-01-31 16:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(default='', max_length=200)),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category/')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 31, 22, 20, 13, 75609)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categories'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
