from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

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