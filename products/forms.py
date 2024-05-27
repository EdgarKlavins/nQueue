from django import forms
from .models import Product, Genre, Year, Author

class ProductForm(forms.ModelForm):
    year = forms.CharField(required=False)
    author = forms.CharField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        genre_choices = [(genre.id, genre.name) for genre in genres]
        
        self.fields['genre'].choices = genre_choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def clean_year(self):
        year_name = self.cleaned_data['year']
        if year_name:
            year, created = Year.objects.get_or_create(year=year_name)
            return year
        return None

    def clean_author(self):
        author_name = self.cleaned_data['author']
        if author_name:
            author, created = Author.objects.get_or_create(name=author_name)
            return author
        return None

    def save(self, commit=True):
        product = super().save(commit=False)

        # Assign the cleaned year and author instances
        product.year = self.cleaned_data.get('year')
        product.author = self.cleaned_data.get('author')

        if commit:
            product.save()
        return product
