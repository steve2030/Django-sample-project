from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
# from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



