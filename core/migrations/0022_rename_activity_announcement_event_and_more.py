# Generated by Django 4.2.2 on 2023-12-18 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_rename_announcements_announcement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='activity',
            new_name='event',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='date',
        ),
    ]
