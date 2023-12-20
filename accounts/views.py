from django.shortcuts import render

from authy.models import User
from core.models import Class


# Create your views here.


def account_home(request):
    staff = User.objects.all().exclude(type='Student/Parent')
    students = User.objects.filter(type='Student/Parent')
    classes = Class.objects.all()
    context = {
        'staff': staff,
        'students': students,
        'classes': classes,
    }
    return render(request, 'accounts/home.html', context)
