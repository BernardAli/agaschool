# Generated by Django 4.2.2 on 2023-12-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_query'),
        ('authy', '0004_alter_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='background_img',
        ),
        migrations.AddField(
            model_name='user',
            name='classes',
            field=models.ManyToManyField(blank=True, related_name='classes', to='core.class'),
        ),
        migrations.AddField(
            model_name='user',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='core.subject'),
        ),
    ]