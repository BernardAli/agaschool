# Generated by Django 4.2.2 on 2023-12-19 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0041_onlineapplication_address_onlineapplication_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('texts', models.CharField(max_length=255)),
                ('paragraph_1', models.TextField()),
                ('paragraph_2', models.TextField()),
                ('paragraph_3', models.TextField(blank=True, null=True)),
                ('paragraph_4', models.TextField(blank=True, null=True)),
                ('paragraph_5', models.TextField(blank=True, null=True)),
                ('paragraph_6', models.TextField(blank=True, null=True)),
                ('paragraph_7', models.TextField(blank=True, null=True)),
                ('paragraph_8', models.TextField(blank=True, null=True)),
                ('paragraph_9', models.TextField(blank=True, null=True)),
                ('prayer', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.articlescategories')),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
    ]