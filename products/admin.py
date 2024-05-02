from django.contrib import admin
from .models import Product, Genre, Author, Year

# Register your models here.
admin.site.register(Product)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Year)