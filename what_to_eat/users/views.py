from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HTTPResponse("User logged in")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

def logout(request):
    request.user.logout()
    return HttpResponse("User logged out")