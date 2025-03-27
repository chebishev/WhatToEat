from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

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
                return render(request, 'core/index.html')
            else:
                return render(request, 'users/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

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

@login_required
def user_profile(request, pk):
    current_user = get_object_or_404(User, pk=pk)

    if current_user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")
    
    return render(request, 'users/profile.html')

def user_edit(request, pk):
    current_user = get_object_or_404(UserModel, pk=pk)

    if current_user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    form = ProfileEditForm(request.POST or None, instance=current_user)

    if form.is_valid():
        instance = form.save(commit=False)
        # TODO: examine this and check if something must be available to change at all!!!
        instance.save()
        return redirect('profile_details', pk=pk)
    else:
        form.fields['preferred_device'].widget.attrs['disabled'] = True

    return render(request, 'auth_app/profile_edit.html', {'form': form})

    return render(request, 'users/profile_edit')

def user_delete(request, pk):
    return render(request, 'user/profile_delete')