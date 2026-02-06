from django.shortcuts import render, get_object_or_404, redirect
from mainapp.models import Product
from .models import Order, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

# Create your views here.
@login_required
def user_dashboard(request):
    products = Product.objects.all()
    # Fetch orders for the logged-in user
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'userdashborad.html', {'products': products, 'orders': orders})

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        
        return JsonResponse({'status': 'success', 'message': 'Product added to cart', 'cart_count': cart.items.count()})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def get_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        items = []
        total_price = 0
        for item in cart.items.all():
            items.append({
                'id': item.id,
                'product_id': item.product.id,
                'title': item.product.title,
                'price': float(item.product.price),
                'quantity': item.quantity,
                'total': float(item.get_total_price()),
                'image_url': item.product.image.url
            })
            total_price += item.get_total_price()
            
        return JsonResponse({'status': 'success', 'items': items, 'total_price': float(total_price)})
    except Cart.DoesNotExist:
        return JsonResponse({'status': 'success', 'items': [], 'total_price': 0})

@login_required
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
        return JsonResponse({'status': 'success', 'message': 'Item removed'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def update_cart_item(request, item_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action')
            cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
            
            if action == 'increase':
                cart_item.quantity += 1
            elif action == 'decrease':
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
            
            cart_item.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def checkout(request):
    if request.method == 'POST':
        try:
            cart = Cart.objects.get(user=request.user)
            if not cart.items.exists():
                return JsonResponse({'status': 'error', 'message': 'Cart is empty'}, status=400)
            
            orders_created = []
            for item in cart.items.all():
                order = Order.objects.create(
                    user=request.user,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.get_total_price(),
                    status='Pending'
                )
                orders_created.append({
                    'id': order.id,
                    'product': order.product.title,
                    'total': float(order.price)
                })
            
            # Clear cart
            cart.items.all().delete()
            
            return JsonResponse({'status': 'success', 'orders': orders_created})
        except Cart.DoesNotExist:
             return JsonResponse({'status': 'error', 'message': 'Cart not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
