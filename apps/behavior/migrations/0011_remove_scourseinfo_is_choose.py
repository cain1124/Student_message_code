# Generated by Django 2.2.2 on 2020-12-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0010_auto_20201213_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scourseinfo',
            name='is_choose',
        ),
    ]
