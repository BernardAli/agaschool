# Generated by Django 4.2.2 on 2023-12-18 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_faqs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FAQs',
            new_name='FAQ',
        ),
    ]
