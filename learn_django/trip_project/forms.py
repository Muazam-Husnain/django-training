from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class Create_User_Form(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValueError('username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValueError('email already exists')
        return email


class Create_Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick_name', 'gender', 'bio']

class Edit_User_Form(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

