# Generated by Django 3.1.7 on 2021-05-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210416_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=256, verbose_name='Comment'),
        ),
    ]
