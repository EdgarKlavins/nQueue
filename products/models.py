from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Year(models.Model):
    year = models.CharField(max_length=14)

    def __str__(self):
        return str(self.year)


class Author(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Product(models.Model):
    genre = models.ForeignKey('Genre', null = True, blank=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    best_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.name
