'''

we create our own form that inherits from user creation form

'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):     # we are making UserRegisterForm which is inheriting from UserCreationForm
    email = forms.EmailField()          #default value is true

    class Meta:
        #we specify a model that we want this form to interact with
        model = User    #when form will validate it will create a new user


        #these are the fields which we want to show
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):         # we want a form that will update our user model
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
