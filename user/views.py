from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm, UserRegisterForm
from .models import UserProfile
from . import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

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

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.get(user=user)
    if user_profile.image:
        image_url = user_profile.image.url
    else:
        image_url = "https://res.cloudinary.com/dlclpbfkf/image/upload/v1682513141/placeholder_kffdba.png"
    return render(request, 'user/user_profile.html', {'user_profile': user_profile, 'image_url': image_url})

@login_required
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('create_profile')
    return redirect('profile', username=request.user.username)
    
@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile', username=request.user.username)
    else:
        form = forms.UserProfileForm(instance=user_profile)
    return render(request, 'user/edit_profile.html', {'form': form})

@login_required
def create_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('user-profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'user/create_profile.html', {'form': form})
