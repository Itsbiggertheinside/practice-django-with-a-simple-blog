from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, UpdateForm

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    context = {'form': form}
    return render(request, 'account/login.html', context)

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        account = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        account.set_password(password)
        account.email = email
        account.save()
        user = authenticate(username=account.username, password=password)
        login(request, user)
        return redirect('home')
    context = {'form': form}
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def profile_view(request):
    posts = request.user.posts.order_by('-created_at')[:3]

    return render(request, 'account/profile.html', context={'posts':posts})

def update_profile_view(request):
    account = request.user
    form = UpdateForm(instance=account)

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            account = form.save()
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'account/update_profile.html', context)