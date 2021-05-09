# Generated by Django 3.1.7 on 2021-03-31 07:51

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210328_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof_img',
            field=django_resized.forms.ResizedImageField(crop=None, default='default_man.jpg', force_format='JPEG', keep_meta=True, quality=75, size=[100, 100], upload_to='profile_pics'),
        ),
    ]
