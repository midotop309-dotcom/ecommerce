from django.shortcuts import render, redirect
from products.models import Product

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id in cart:
        item = cart[product_id]
        try:
            product = Product.objects.get(id=product_id)
            item_total = float(item['price']) * item['quantity']
            total_price = total_price + item_total
            
            cart_items.append({
                'product': product,
                'quantity': item['quantity'],
                'item_total': item_total
            })
        except Product.DoesNotExist:
            pass

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    p_id = str(product_id)

    if p_id in cart:
        cart[p_id]['quantity'] = cart[p_id]['quantity'] + 1
    else:
        cart[p_id] = {
            'price': float(product.price),
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('cart:cart_detail')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)

    if p_id in cart:
        if cart[p_id]['quantity'] > 1:
            cart[p_id]['quantity'] = cart[p_id]['quantity'] - 1
        else:
            del cart[p_id]
            
        request.session['cart'] = cart

    return redirect('cart:cart_detail')