# Generated by Django 2.2.2 on 2020-12-01 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='student_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.DepartmentInfo', verbose_name='所属学院'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='student_major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.MajorInfo', verbose_name='所属专业'),
        ),
    ]
