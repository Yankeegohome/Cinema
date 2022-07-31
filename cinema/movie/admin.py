from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}
    save_on_top = True
    list_display = ('id', 'title', 'url', 'category', 'get_poster', 'is_published' )
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'genre')

    def get_poster(self, obj):
        if obj.poster:
            return mark_safe(f'<img src={obj.poster.url} width="50">')
        return "Постер не добавлен"



admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)