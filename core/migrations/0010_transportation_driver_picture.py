# Generated by Django 4.2.2 on 2023-10-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_transportation_driver_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='driver_picture',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
    ]
