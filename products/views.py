from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Comment
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, CommentForm
from django.contrib.auth import get_user_model


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comment_form = CommentForm()
    comments = product.comments.all().order_by('-created_at')
    context = {
        'product': product,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'products/product_detail.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.author = request.user
                product.save()
                return redirect('products:products_list')
        else:
            form = ProductForm()
            context = {'form': form}
            return render(request, 'products/create.html', context)
    return redirect('accounts:login')


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=pk)
        if request.user == product.author:
            product.delete()
            return redirect('products:products_list')
        return redirect('products:product_detail', product.pk)
    return redirect('accounts:login')


@require_http_methods(['POST', 'GET'])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.author:
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
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
    return redirect('products:product_detail', pk)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.id).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect('products:products_list')
    return redirect('accounts:login')


@require_POST
def create_comment(request, pk):
    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product_id = pk
            comment.author = request.user
            comment.save()
        return redirect('products:product_detail', pk)
    return redirect('accounts:login')


@require_POST
def delete_comment(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.author:
            comment.delete()
        return redirect('products:product_detail', pk)
    return redirect('products:products_list')
