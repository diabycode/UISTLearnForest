from django.contrib import admin

from .models import *


# add Cours to admin panel
@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_at')


# add Section to admin panel
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'cours')


# add Video to admin panel
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_source', 'description')


# add Article to admin panel
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('content',)