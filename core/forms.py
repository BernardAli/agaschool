from django import forms
from .models import OnlineApplication


class OnlineApplicationForm(forms.ModelForm):
    class Meta:
        model = OnlineApplication
        fields = "__all__"
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
