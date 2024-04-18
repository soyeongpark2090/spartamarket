from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # request.uer은 로그인한 사용자 ->따라서 여기서는 쓸 수 없음
            auth_login(request, user)
            return redirect('products:products_list')
    else:
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


@require_http_methods(['POST', 'GET'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('products:products_list')

    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('products:products_list')
