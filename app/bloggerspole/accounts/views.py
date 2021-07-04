from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.auth import login, logout

def signup_account(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blogs:index_path')
    else:    
        form = SignupForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_account(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blogs:index_path')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_account(request):
    logout(request)
    return redirect('landing_path')
