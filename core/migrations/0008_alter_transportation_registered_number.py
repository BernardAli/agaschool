# Generated by Django 4.2.2 on 2023-10-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_transportation_alter_gallery_image_alter_games_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='registered_number',
            field=models.CharField(max_length=15),
        ),
    ]
