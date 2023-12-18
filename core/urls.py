from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_page, name='home'),
    path("about/", views.about_us, name='about'),
    path('create_testimony/', views.CreateTestimonyView.as_view(), name='create_testimony'),
    path("history/", views.history, name='history'),
    path("fees/", views.fees, name='fees'),
    path("library/", views.library, name='library'),
    path("awards/", views.awards, name='awards'),
    path("counselors/", views.counselors, name='counselors'),
    path("schedule_visit/", views.schedule_visit, name='schedule_visit'),
    path("newsletter/", views.newsletter, name='newsletter'),
    path("calendar/", views.calendar, name='calendar'),
    path("management/", views.management, name='management'),
    path("admission/", views.CreateAdmissionView.as_view(), name='admission'),
    path("teachers/", views.teachers, name='teachers'),
    path("counselors/", views.counselors, name='counselors'),
    path("classes/", views.classes, name='classes'),
    path("class_detail/<slug:slug>/", views.class_detail, name='class_detail'),
    path("contact/", views.contact, name='contact'),
    path("academics/", views.academics, name='academics'),
    path("placement_test/", views.placement_test, name='placement_test'),
    path("games/", views.games, name='games'),
    path("gallery/", views.gallery, name='gallery'),
    path("articles/", views.articles, name='articles'),
    path("article_details/<int:id>/", views.article_details, name='article_details'),
    path("journal/", views.JournalListView.as_view(), name='journal'),
    path("journal_details/<int:pk>/", views.JournalDetailView.as_view(), name='journal_details'),
    path("careers/", views.careers, name='careers'),
    path('careers/<int:career_id>/', views.career_detail, name='career_detail'),
    path("store/", views.store, name='store'),
    path("transportation/", views.transportation, name='transportation'),
    path("transportation_details/<int:id>/", views.transportation_details, name='transportation_details'),
    path("remote/", views.remote, name='remote'),
]