from django.shortcuts import render, get_object_or_404

from authy.models import User
from core.models import Class, Subject


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


def all_students(request):
    students = User.objects.filter(type='Student/Parent')
    context = {
        'students': students,
    }
    return render(request, 'accounts/all_students.html', context)


def all_staff(request):
    staff = User.objects.all().exclude(type='Student/Parent')
    context = {
        'staff': staff,
    }
    return render(request, 'accounts/all_staff.html', context)


def subjects(request):
    all_subjects = Subject.objects.all()
    context = {
        'subjects': all_subjects,
    }
    return render(request, 'accounts/subjects.html', context)


def all_classes(request):
    classes = Class.objects.all()
    context = {
        'classes': classes,
    }
    return render(request, 'accounts/all_classes.html', context)


def account_class_detail(request, slug):
    name = Class.objects.get(slug=slug)
    students = User.objects.filter(classes=name.id).filter(type='Student/Parent').order_by('last_name', 'first_name')
    total_students = User.objects.filter(classes=name.id).filter(type='Student/Parent').count()
    context = {
        'name': name,
        'students': students,
        'total_students': total_students,
    }
    return render(request, 'accounts/account_class_detail.html', context)


def account_profile(request, username):
    profile = get_object_or_404(User, username=username)
    context = {
        'profile': profile,
    }
    return render(request, 'accounts/account_profile.html', context)
