# Generated by Django 3.1.7 on 2021-05-03 14:54

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210331_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof_img',
            field=django_resized.forms.ResizedImageField(crop=None, default='profile_pics/default_man.jpg', force_format='JPEG', keep_meta=True, quality=75, size=[100, 100], upload_to='profile_pics'),
        ),
    ]
