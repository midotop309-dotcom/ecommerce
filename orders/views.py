from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from products.models import Product

def create_order(request):
    cart = request.session.get('cart', {})
    
    if not cart:
        return redirect('products:product_list')

    total = 0
    for item in cart.values():
        total = total + (float(item['price']) * item['quantity'])

    order = Order.objects.create(total_price=total, status='Pending')

    for product_id in cart:
        item = cart[product_id]
        product = Product.objects.get(id=product_id)
        
        OrderItem.objects.create(
            order=order,
            product=product,
            price=item['price'],
            quantity=item['quantity']
        )

    request.session['cart'] = {}
    return redirect('orders:order_list')

def order_list(request):
    orders = Order.objects.all().order_by('-id') 
    return render(request, 'orders/order_list.html', {'orders': orders})

def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Confirmed'
    order.save()
    return redirect('orders:order_list')

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Cancelled'
    order.save()
    return redirect('orders:order_list')