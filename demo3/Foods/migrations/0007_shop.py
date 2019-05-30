# Generated by Django 2.2.1 on 2019-05-30 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0006_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='')),
                ('num', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
    ]
