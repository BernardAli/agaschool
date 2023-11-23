from django import forms
from django.contrib.auth import models
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm

from .models import User


class MyUserCreationForm(UserCreationForm):
    avatar = forms.FileField(widget=forms.FileInput(attrs={'accept': ".jpg, .jpeg, .png"}), required=True)
    background_img = forms.FileField(widget=forms.FileInput(attrs={'accept': ".jpg, .jpeg, .png"}), required=True)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2',
                  'phone', 'residence', 'GPS_Address', 'region']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', "phone", "avatar", "region",  "facebook_url", "twitter_url", "instagram_url",
                  "linkedin_url", "website_url", "background_img"]
        widgets = {
            "user_type": forms.Select(attrs={'onchange': "update();"}),
        }