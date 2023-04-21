from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Cuisine

# Create your views here.

class CuisineListView(ListView):
    model = Cuisine
    template_name = 'cuisine/home.html'
    context_object_name = 'cuisines'
  

def home(request):
    cuisines = Cuisine.objects.all()
    context = {
        'cuisines': cuisines
    }
    return render(request, 'cuisine/home.html', context)


class CuisineDetailView(DetailView):
    model = Cuisine


class CuisineCreateView(LoginRequiredMixin, CreateView) :
    model = Cuisine
    fields = ['title', 'description'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CuisineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView) :
    model = Cuisine
    fields = ['title', 'description'] 

    def test_func(self):
        cuisine = self.get_object()
        return self.request.user == cuisine.author


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CuisineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView) :
    model = Cuisine
    success_url = reverse_lazy('home')

    def test_func(self):
        cuisine = self.get_object()
        return self.request.user == cuisine.author


    



def about(request):
    return render(request, 'cuisine/about.html')
