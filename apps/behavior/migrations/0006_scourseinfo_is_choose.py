# Generated by Django 2.2.2 on 2020-12-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0005_scourseinfo_course_cj'),
    ]

    operations = [
        migrations.AddField(
            model_name='scourseinfo',
            name='is_choose',
            field=models.BooleanField(default=False, verbose_name='选课状态'),
        ),
    ]
