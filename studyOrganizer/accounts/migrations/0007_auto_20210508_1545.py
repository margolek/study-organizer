# Generated by Django 3.1.7 on 2021-05-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210503_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof_img',
            field=models.ImageField(default='profile_pics/default_man.jpg', upload_to='profile_pics'),
        ),
    ]
