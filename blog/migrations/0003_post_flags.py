# Generated by Django 3.2 on 2022-03-27 03:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='flags',
            field=models.ManyToManyField(blank=True, related_name='blogpost_flag', to=settings.AUTH_USER_MODEL),
        ),
    ]
