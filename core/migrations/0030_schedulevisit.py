# Generated by Django 4.2.2 on 2023-12-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_rename_faqs_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=125)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
