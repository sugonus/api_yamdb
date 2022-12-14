from django.contrib import admin

from .models import Title, Category, Genre

admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'genre', 'year', 'rating')
    search_fields = ('name',)
    list_filter = ('rating',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
