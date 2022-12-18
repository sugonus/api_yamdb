from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Title, Category, Genre, User, GenreTitle, Comment, Review


class GenreTitleInline(admin.TabularInline):
    model = Title.genre.through


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'category',
        )


class TitleAdmin(ImportExportModelAdmin):
    resource_classes = [TitleResource]
    list_display = ('name', 'year', 'description', 'category',)
    search_fields = ('name',)
    list_filter = ('id',)
    inlines = [GenreTitleInline]


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = (
            'id',
            'name',
            'slug',
        )


class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]
    list_display = ('id', 'name', 'slug',)
    search_fields = ('name',)
    list_filter = ('id',)


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
        )


class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    list_filter = ('id',)


class GenreTitleResource(resources.ModelResource):
    class Meta:
        model = GenreTitle
        fields = (
            'id',
            'title_id',
            'genre_id',
        )


class GenreTitleAdmin(ImportExportModelAdmin):
    resource_classes = [GenreTitleResource]
    list_filter = ('id',)


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'role',
            'bio',
        )


class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]
    list_display = (
        'id',
        'username',
        'email',
    )


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
admin.site.register(Review)
admin.site.register(Comment)
