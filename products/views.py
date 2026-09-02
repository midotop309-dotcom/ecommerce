from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    q = request.GET.get('q')
    cat_id = request.GET.get('category')
    
    products = Product.objects.all()

    if q:
        products = products.filter(name__icontains=q)

    if cat_id:
        products = products.filter(category_id=cat_id)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'query': q,
        'selected_category': cat_id,
    }

    return render(request, 'products/product_list.html', context)
