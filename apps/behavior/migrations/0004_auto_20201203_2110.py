# Generated by Django 2.2.2 on 2020-12-03 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0003_studentmessage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmessage',
            old_name='messa_status',
            new_name='message_status',
        ),
    ]