from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

USER_STATUS = (
    ('Active', 'Active'),
    ('Suspended', 'Suspended'),
    ('Blocked', 'Blocked'),
)

USER_TYPE = (
    ('Student/Parent', 'Student/Parent'),
    ('Teacher', 'Teacher'),
)

MARITAL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
)

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

REGION_CHOICE = (
    ('Northern', 'Northern'),
    ('Ashanti', 'Ashanti'),
    ('Western', 'Western'),
    ('Volta', 'Volta'),
    ('Eastern', 'Eastern'),
    ('Upper West', 'Upper West'),
    ('Central', 'Central'),
    ('Upper East', 'Upper East'),
    ('Greater Accra', 'Greater Accra'),
    ('Savannah', 'Savannah'),
    ('North East', 'North East'),
    ('Bono East', 'Bono East'),
    ('Oti', 'Oti'),
    ('Ahafo', 'Ahafo'),
    ('Bono', 'Bono'),
    ('Western North', 'Western North'),
)


class User(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(null=True, default="default.jpg")
    background_img = models.ImageField(default='home-bg.jpg', upload_to='background_pics')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE, null=True, blank=True)
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS, default='Single')
    region = models.CharField(max_length=100, choices=REGION_CHOICE, null=True, blank=True)
    residence = models.CharField(max_length=100)
    GPS_Address = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100, default='Ghanaian')

    created = models.DateField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    website_url = models.URLField(max_length=255, blank=True, null=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])