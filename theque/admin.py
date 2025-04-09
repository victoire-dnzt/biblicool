from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating')
    search_fields = ('title', 'author')


    def cover_image(self, obj):
        return obj.cover.url if obj.cover else 'No Image'
        cover_image.short_description = 'Cover'
