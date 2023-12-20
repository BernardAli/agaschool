from django.urls import path
from .views import account_home, all_students

urlpatterns = [
    path('', account_home, name='account_home'),
    path('all_students', all_students, name='all_students'),
]