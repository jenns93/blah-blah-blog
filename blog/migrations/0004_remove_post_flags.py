# Generated by Django 3.2 on 2022-03-27 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_flags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='flags',
        ),
    ]