# Generated by Django 4.2.2 on 2023-12-18 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_otherfees'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OtherFees',
            new_name='OtherFee',
        ),
    ]