from django.shortcuts import render
from mainapp.models import Product
from .models import Order

# Create your views here.
def user_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all().order_by('-date')
    return render(request, 'userdashborad.html', {'products': products, 'orders': orders})


def user_footer(request):
    return render(request, 'userfooter.html')