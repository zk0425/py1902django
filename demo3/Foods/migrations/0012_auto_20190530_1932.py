# Generated by Django 2.2.1 on 2019-05-30 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0011_auto_20190530_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='deels',
            new_name='deeds',
        ),
    ]