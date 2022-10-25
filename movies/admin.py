from django.contrib import admin
from .models import*
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url',)
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}
    ordering = ['name']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'get_html_photo',)
    list_display_links = ('name',)
    ordering = ['name']

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}
    ordering = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_html_photo', 'year', 'draft',)
    list_display_links = ('title',)
    prepopulated_fields = {'url': ('title',)}
    ordering = ['title']

    def get_html_photo(self, object):
        if object.poster:
            return mark_safe(f"<img src='{object.poster.url}' width=50>")

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'movie', 'get_html_photo',)
    list_display_links = ('title',)
    ordering = ['title']

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")



@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'movie',)
    list_display_links = ('name',)
    ordering = ['name']