from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Profile
from . import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import UpdateView
from .forms import ProfileUpdateForm
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
def profile_view(request, pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)


@login_required
def profile_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if not hasattr(user, 'profile'):
        return redirect('profile')
    
    profile = user.profile

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', pk=pk)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'user/edit_profile.html', context)