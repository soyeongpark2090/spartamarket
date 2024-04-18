from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


def products_list(request):
    return render(request, 'products/products_list.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('products:products_list')
    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, 'products/create.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return redirect('products:products_list')


@require_http_methods(['POST', 'GET'])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', pk)
    else:
        form = ProductForm(instance=product)
        context = {
            'form': form,
            'product': product
        }
        return render(request, 'products/update.html', context)
