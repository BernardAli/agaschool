# Generated by Django 4.2.2 on 2023-10-02 11:22

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('avatar', models.ImageField(default='default.jpg', null=True, upload_to='')),
                ('background_img', models.ImageField(default='home-bg.jpg', upload_to='background_pics')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Female'), ('Female', 'Female')], max_length=100, null=True)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=100)),
                ('region', models.CharField(blank=True, choices=[('Northern', 'Northern'), ('Ashanti', 'Ashanti'), ('Western', 'Western'), ('Volta', 'Volta'), ('Eastern', 'Eastern'), ('Upper West', 'Upper West'), ('Central', 'Central'), ('Upper East', 'Upper East'), ('Greater Accra', 'Greater Accra'), ('Savannah', 'Savannah'), ('North East', 'North East'), ('Bono East', 'Bono East'), ('Oti', 'Oti'), ('Ahafo', 'Ahafo'), ('Bono', 'Bono'), ('Western North', 'Western North')], max_length=100, null=True)),
                ('nationality', models.CharField(default='Ghanaian', max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('registration_fee', models.PositiveIntegerField(blank=True, default=0.0, null=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=20)),
                ('facebook_url', models.URLField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.URLField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.URLField(blank=True, max_length=255, null=True)),
                ('website_url', models.URLField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
