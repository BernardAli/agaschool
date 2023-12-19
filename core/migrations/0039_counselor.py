# Generated by Django 4.2.2 on 2023-12-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_management'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
