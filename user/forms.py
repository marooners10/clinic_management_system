from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    #defining how our form will look like
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        

#user update form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email'] 
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']