from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView

from accounts.forms import SubjectForm, ClassForm
from accounts.models import CashCenter, IncomeExpenditure
from authy.forms import MyUserCreationForm
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


def add_students(request):
    form = MyUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/add_students.html', context)


def all_staff(request):
    staff = User.objects.all().exclude(type='Student/Parent')
    context = {
        'staff': staff,
    }
    return render(request, 'accounts/all_staff.html', context)


def add_staff(request):
    form = MyUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/add_staff.html', context)


def subjects(request):
    all_subjects = Subject.objects.all()
    context = {
        'subjects': all_subjects,
    }
    return render(request, 'accounts/subjects.html', context)


def add_subject(request):
    form = SubjectForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/add_subject.html', context)


def all_classes(request):
    classes = Class.objects.all()
    context = {
        'classes': classes,
    }
    return render(request, 'accounts/all_classes.html', context)


def add_class(request):
    form = ClassForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/add_class.html', context)


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


class CashCenterListView(ListView):
    template_name = 'accounts/cash_center_list.html'
    model = CashCenter
    context_object_name = 'cash_centers'


class CashCenterDetailView(DetailView):
    model = CashCenter
    template_name = 'accounts/cash_center_details.html'


class CashCenterCreateView(CreateView):
    model = CashCenter
    template_name = 'accounts/cash_center_create.html'
    fields = "__all__"
    success_url = reverse_lazy("cash_center_list")


class CashCenterUpdateView(UpdateView):
    model = CashCenter
    context_object_name = 'cash_center'
    template_name = 'accounts/cash_center_update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy("cash_center_list")


class CashCenterDeleteView(DeleteView):
    model = CashCenter
    context_object_name = 'cash_center'
    template_name = 'accounts/cash_center_delete.html'
    success_url = reverse_lazy("category_list")


def income_expenditure(request):
    income_expenditures = IncomeExpenditure.objects.all()
    context = {
        'income_expenditures': income_expenditures,
    }
    return render(request, 'accounts/income_expenditure.html', context)


class IECreateView(CreateView):
    model = IncomeExpenditure
    template_name = 'accounts/income_expenditure_create.html'
    fields = ['center', 'item_name', 'balance']
    success_url = reverse_lazy("income_expenditure")

