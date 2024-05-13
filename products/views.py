from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Genre

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    genre = None
    sort = None
    direction = None
    best_sellers = False

    if request.GET:

        
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'year':
                sortkey = '-year' if 'direction' in request.GET and request.GET['direction'] == 'desc' else 'year'
            elif sortkey == 'rating':
                 sortkey = '-rating' if 'direction' in request.GET and request.GET['direction'] == 'desc' else 'rating'


            if 'direction' in request.GET:
                direction = request.GET['direction']

            products = products.order_by(sortkey)
            

        if 'genre' in request.GET:
            genre = request.GET.get('genre').split(',')
            products = products.filter(genre__name__in=genre)
            genre = Genre.objects.filter(name__in=genre)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products.exists():
                messages.warning(request, "No products found matching the search criteria.")
        

        if 'best_seller' in request.GET and request.GET['best_seller'] == 'true':
            products = products.filter(best_seller=True)
            best_sellers = True


    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_genre': genre,
        'current_sorting': current_sorting,
        'best_sellers': best_sellers,
    }

    return render(request, 'products/products.html', context)

def product_description(request, product_id):
    """ A view to show separate product description  """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_description.html', context)

