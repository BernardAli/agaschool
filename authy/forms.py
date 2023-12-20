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


general_fields = ['full_name', "phone", 'email', "avatar", 'residence', 'GPS_Address', "region", 'nationality']


class StudentForm(ModelForm):
    class Meta:
        model = User
        fields = general_fields
        widgets = {
            "user_type": forms.Select(attrs={'onchange': "update();"}),
        }


class TeacherForm(ModelForm):
    class Meta:
        model = User
        fields = general_fields + ["facebook_url", "twitter_url", "instagram_url", "linkedin_url", "website_url"]
        widgets = {
            "user_type": forms.Select(attrs={'onchange': "update();"}),
        }
