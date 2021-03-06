# Generated by Django 2.2.2 on 2020-12-13 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0006_scourseinfo_is_choose'),
    ]

    operations = [
        migrations.AddField(
            model_name='scourseinfo',
            name='type',
            field=models.CharField(blank=True, choices=[('申请', '申请'), ('退选', '退选')], default='申请', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='scourseinfo',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseInfo', verbose_name='申请课程'),
        ),
    ]
