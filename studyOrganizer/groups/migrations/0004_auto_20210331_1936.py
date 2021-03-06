# Generated by Django 3.1.7 on 2021-03-31 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_auto_20210331_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='image',
        ),
        migrations.AddField(
            model_name='group',
            name='description_html',
            field=models.TextField(blank=True, default='', editable=False),
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='groups.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('group', 'user')},
            },
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='groups.GroupMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
