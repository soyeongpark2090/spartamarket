from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required


def products_list(request):
    return render(request, 'products/products_list.html')


def product_detail(request, pk):
    product = get_object_or_404()
    return render(request, 'products/product_detail.html')
