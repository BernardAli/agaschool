from django.contrib import admin
from .models import (
    Class, GalleryCategory, Gallery, GamesCategory, Games, Transportation,
    Route, OurCareer, Articles, ArticlesCategories, Subject)

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