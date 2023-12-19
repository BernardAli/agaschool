# Generated by Django 4.2.2 on 2023-12-19 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_submitassignment_submitted_on_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.class')),
            ],
        ),
    ]
