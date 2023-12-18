from django.contrib import admin
from .models import (
    Class, GalleryCategory, Gallery, GamesCategory, Games, Transportation,
    Route, OurCareer, Articles, ArticlesCategories, Subject, AdmissionForm, OnlineApplication, Journal, Calendar,
    Announcement, OtherFee, Library, FAQ, ScheduleVisit, Newsletter, Assignment)

# Register your models here.


admin.site.register(Class)
admin.site.register(GalleryCategory)
admin.site.register(Gallery)
admin.site.register(GamesCategory)
admin.site.register(Games)
admin.site.register(Transportation)
admin.site.register(Route)
admin.site.register(OurCareer)
admin.site.register(Articles)
admin.site.register(ArticlesCategories)
admin.site.register(Subject)
admin.site.register(AdmissionForm)
admin.site.register(OnlineApplication)
admin.site.register(Journal)
admin.site.register(Calendar)
admin.site.register(Announcement)
admin.site.register(OtherFee)
admin.site.register(Library)
admin.site.register(FAQ)
admin.site.register(ScheduleVisit)
admin.site.register(Newsletter)
admin.site.register(Assignment)