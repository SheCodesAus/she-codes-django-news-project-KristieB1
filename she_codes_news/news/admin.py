from django.contrib import admin
from .models import Category, NewsStory
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title',  'content']

admin.site.register(NewsStory, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category, CategoryAdmin)