from django.forms import ModelForm

from core.models import Subject, Class


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'