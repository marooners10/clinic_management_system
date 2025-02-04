from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm#user registration form provided by django
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages 

# Create your views here.

#creating form and access with register.html
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')# get username from form 
            messages.success(request, f'Account has been created for {username}. Continue to login.')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
    }# value of form is form
    return render(request, 'user/register.html', context) 



#for logout
@login_required
def user_logout(request):
    if request.method in ['GET', 'POST']:
        logout(request)
        return redirect('user-login')  # Redirect to the login page
    

#for user profile
def profile(request):
    return render(request, 'user/profile.html')


#for editing profile
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # instance helps to pre-fill the form
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile) 
    context = { #passing multiple form 
        'user_form': user_form,
        'profile_form' : profile_form
    }
    return render(request, 'user/profile_update.html', context)