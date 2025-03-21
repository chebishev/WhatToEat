from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # from django.contrib.auth
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # from django.contrib.auth
                login(request, user)
                return HttpResponse("User logged in")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def index(request):
    return render(request, 'users/index.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html')
    
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})