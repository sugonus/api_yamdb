from django.contrib import admin
from .models import Title, Category, Genre, GenreTitle, Comment, Review
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',
                    'role', 'bio', 'first_name', 'last_name')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class GenreTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_id', 'genre_id')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review_id', 'text', 'author', 'pub_date')


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
