from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "w3-input w3-border"}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': "w3-input w3-border"}))

class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': "w3-input w3-border"}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': "w3-input w3-border"}
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data['password2']
    

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']