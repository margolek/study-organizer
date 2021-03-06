# Generated by Django 3.1.7 on 2021-03-28 19:09

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210328_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof_img',
            field=django_resized.forms.ResizedImageField(crop=['center'], default='default_man.jpg', force_format='JPEG', keep_meta=True, quality=75, size=[100, 100], upload_to='profile_pics'),
        ),
    ]
