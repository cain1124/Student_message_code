# Generated by Django 2.2.2 on 2020-12-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0013_auto_20201213_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scourseinfo',
            name='course_cj',
            field=models.IntegerField(blank=True, null=True, verbose_name='课程成绩'),
        ),
    ]
