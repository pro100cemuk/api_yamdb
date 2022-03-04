from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Genre, Titles, User

admin.site.register(User, UserAdmin)
EMPTY_CONST = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('slug', 'name')
    list_filter = ('slug', 'name')
    empty_value_display = EMPTY_CONST


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('slug', 'name')
    list_filter = ('slug', 'name')
    empty_value_display = EMPTY_CONST


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'category',
        # 'genre',
        'year'
    )
    search_fields = ('year', 'category', 'genre', 'name')
    list_filter = ('year', 'category', 'genre')
    empty_value_display = EMPTY_CONST
