from django.urls import path
from .views import (account_home, all_students, all_staff, all_classes,
                    account_profile, account_class_detail, subjects, add_students, add_staff, add_subject, add_class,
                    CashCenterListView, CashCenterDetailView, CashCenterCreateView, CashCenterUpdateView,
                    CashCenterDeleteView, income_expenditure, IECreateView)

urlpatterns = [
    path('', account_home, name='account_home'),
    path('all_students', all_students, name='all_students'),
    path('all_staff', all_staff, name='all_staff'),
    path('all_classes', all_classes, name='all_classes'),
    path('add_class', add_class, name='add_class'),
    path('subjects', subjects, name='subjects'),
    path('add_subject', add_subject, name='add_subject'),
    path('add_students', add_students, name='add_students'),
    path('add_staff', add_staff, name='add_staff'),

    # cash centers
    path('cash_center_list', CashCenterListView.as_view(), name='cash_center_list'),
    path('cash_center_details/<int:pk>/', CashCenterDetailView.as_view(), name='cash_center_details'),
    path('cash_center_create', CashCenterCreateView.as_view(), name='cash_center_create'),
    path('cash_center_update/<int:pk>/', CashCenterUpdateView.as_view(), name='cash_center_update'),
    path('cash_center_delete/<int:pk>/', CashCenterDeleteView.as_view(), name='cash_center_delete'),
    path('account_profile/<username>/', account_profile, name='account_profile'),
    path("account_class_detail/<slug:slug>/", account_class_detail, name='account_class_detail'),

    # Fees Payments
    path('income_expenditure', income_expenditure, name='income_expenditure'),
    path('income_expenditure_create', IECreateView.as_view(), name='income_expenditure_create'),
]