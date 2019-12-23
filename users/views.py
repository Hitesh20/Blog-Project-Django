from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required      ## to get to profile page when we are loged in
'''
different types of messages are:
messages.debug
messages.info
messages.success
messages.warning
messages.error


'''


# Create your views here.
def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)#this will create a form with post parameters
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  #grabbing username that is submitted  ##cleaned data is dictionary
            messages.success(request, f'Your account has been created! You are now able to login')         #using f strings here
            return redirect('login')
    else:
        #form = UserCreationForm(request.POST)  # this will create a blank form
        form = UserRegisterForm(request.POST)
    return render(request, 'users/register.html', {'form':form})
    #in 3rd parameter we just pass form as context to the template so that we can access the form from within the template



@login_required    #adding functionality
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)

















