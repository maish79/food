from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created, please login")
            form.save()
            return redirect('login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required()
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'user/profile.html', context)


    
@login_required()
def update_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user/update_profile.html', {'form': form})