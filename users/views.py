from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST, require_http_methods


def profile(request, username):
    if request.user.is_authenticated:
        if get_user_model().objects.filter(username=username).exists():
            member = get_object_or_404(get_user_model(), username=username)
            products = member.products.all()
            likes = member.like_articles.all()
            followers = member.followers.all().count()
            followings = member.followings.all().count()
            context = {
                'member': member,
                'products': products,
                'likes': likes,
                'followers': followers,
                'followings': followings,
            }
            return render(request, 'users/profile.html', context)
        return redirect('products:products_list')
    return redirect('products:products_list')


def follow(request, username):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), username=username)
        if request.user != member:
            if request.user not in member.followers.all():
                member.followers.add(request.user)
            else:
                member.followers.remove(request.user)
            return redirect('users:profile', username=username)
        return redirect('products:products_list')
    return redirect('accounts:login')
