# Generated by Django 3.1.7 on 2021-03-31 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20210331_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description_html',
        ),
    ]
