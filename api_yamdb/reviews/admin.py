from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin

from .models import Title, Category, Genre

admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'genre', 'year', 'rating')
    search_fields = ('name',)
    list_filter = ('rating',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
