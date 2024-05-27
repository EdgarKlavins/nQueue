from django import forms
from .models import Product, Genre


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