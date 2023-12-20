from django.urls import path
from .views import account_home, all_students, all_staff, all_classes, account_profile

urlpatterns = [
    path('', account_home, name='account_home'),
    path('all_students', all_students, name='all_students'),
    path('all_staff', all_staff, name='all_staff'),
    path('all_classes', all_classes, name='all_classes'),
    path('account_profile/<username>/', account_profile, name='account_profile'),
]