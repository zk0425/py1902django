# Generated by Django 2.2.1 on 2019-05-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0010_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
