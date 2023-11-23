# Generated by Django 4.2.2 on 2023-10-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_ourcareer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55, unique=True)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('testimony', models.TextField()),
            ],
        ),
    ]
