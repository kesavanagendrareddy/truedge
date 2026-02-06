from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import Product
from django.contrib.auth.models import User

# Create your views here.

from userapp.models import Order

def admin_dashboard(request):
    orders = Order.objects.all().order_by('-date')
    return render(request, 'admindashboard.html', {'orders': orders})

def admin_login(request):
    return render(request, 'adminlogin.html')

def products(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')

        Product.objects.create(
            image=image,
            title=title,
            description=description,
            price=price
        )
        return redirect('products')

    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        
        product.save()
        return redirect('products')
    return redirect('products')

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return redirect('products')

def view_users(request):
    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})
