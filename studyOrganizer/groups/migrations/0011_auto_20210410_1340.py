# Generated by Django 3.1.7 on 2021-04-10 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0010_groupcomments_groupcontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupcontent',
            name='author',
        ),
        migrations.RemoveField(
            model_name='groupcontent',
            name='group',
        ),
        migrations.DeleteModel(
            name='GroupComments',
        ),
        migrations.DeleteModel(
            name='GroupContent',
        ),
    ]
