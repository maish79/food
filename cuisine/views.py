from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from .models import Cuisine, Comment, Contact
from .forms import CommentForm, ContactForm

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
    fields = ['title', 'description','ingredients', 'image'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CuisineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView) :
    model = Cuisine
    fields = ['title', 'description','ingredients', 'image'] 

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


@login_required
def add_comment(request, cuisine_id):
    cuisine = get_object_or_404(Cuisine, pk=cuisine_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.cuisine = cuisine
            comment.author = request.user
            comment.save()
            return redirect('cuisine-detail', pk=cuisine_id)
    else:
        form = CommentForm()
    return render(request, 'cuisine/comment_form.html', {'form': form}) 

@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user or request.user.is_staff:
        comment.delete()
    return redirect('cuisine-detail', pk=comment.cuisine.pk)

def contact_view(request):
    # If the form has been submitted...
    if request.method == 'POST':
        # Create a new Contact object with the submitted form data
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject']
            )
            # Redirect to a "success" page
            return redirect('success')
    # If the form hasn't been submitted, render the empty form
    else:
        form = ContactForm()
    return render(request, 'cuisine/contact.html', {'form': form})

def success_view(request):
    return render(request, 'cuisine/success.html')
    


