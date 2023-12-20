from django.shortcuts import render

from authy.models import User


# Create your views here.


def account_home(request):
    staff = User.objects.all().exclude(type='Student/Parent')
    students = User.objects.filter(type='Student/Parent')
    context = {
        'staff': staff,
        'students': students
    }
    return render(request, 'accounts/home.html', context)
