
from django.contrib import admin
from .models import Gallery, Review


class ReviewInline(admin.TabularInline):
    model = Review


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ReviewInline, ]
    list_display = ("title", "author", "price",)


admin.site.register(Gallery, GalleryAdmin)
