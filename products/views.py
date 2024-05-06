from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Genre

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    genre = None

    if request.GET:

        if 'genre' in request.GET:
            genre = request.GET.get('genre').split(',')
            products = products.filter(genre__name__in=genre)
            genre = Genre.objects.filter(name__in=genre)




        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))
            
            queries =Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
            if not products.exists():
                messages.warning(request, "No products found matching the search criteria.")

    context = {
        'products': products,
        'search_term' : query,
        'current_genre' : genre,
    }

    return render(request, 'products/products.html', context)


def product_description(request, product_id):
    """ A view to show seperate product description  """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_description.html', context)