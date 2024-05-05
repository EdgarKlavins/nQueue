from django.contrib import admin
from .models import Product, Genre, Author, Year

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'year',
        'genre',
        'price',
        'rating',
        'image_url',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Year)