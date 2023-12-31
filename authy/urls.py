from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # passwords
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='authy/password_reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='authy/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='authy/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='authy/password_reset_complete.html'), name='password_reset_complete'),


    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/edit/', views.update_user, name='edit_profile'),
    path('<username>/update_teacher/', views.update_teacher, name='update_teacher'),
    path('<username>/update_student/', views.update_student, name='update_student'),
]