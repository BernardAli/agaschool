from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.views.generic import DeleteView

from authy.forms import MyUserCreationForm, UserForm
from authy.models import User


def register_user(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST['full_name']
        username = request.POST.get("username")
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        residence = request.POST['residence']
        GPS_Address = request.POST['GPS_Address']
        phone = request.POST['phone']
        region = request.POST['region']

        if username == "":
            messages.info(request, "Username is required")

        if residence == "":
            messages.info(request, "Location is required")

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect('register')
            elif len(password) < 5:
                messages.info(request, "Password too short")
                return redirect('register')
            else:
                user = User.objects.create_user(full_name=name, username=username, email=email, password=password,
                                                residence=residence, phone=phone, region=region, GPS_Address=GPS_Address)
                user.save()
                messages.success(request, f'Your account has been created! You can login now')
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'authy/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, f"{email} does not exist")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f"{email} or password does not exist")

    context = {
        'page': page,
    }

    return render(request, 'authy/login.html', context)