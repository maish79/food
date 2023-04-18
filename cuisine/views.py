from django.shortcuts import render, HttpResponse

# Create your views here.

cuisines = [
    {
        'title': 'doner',
        'ingredients': 'chicken, salad, curry',
        'prep_time' : 'one hour',
        'created_at' : 'jan 13, 2023'
    },
     {
        'title': 'hamburger',
        'ingredients': 'beef, salad, curry, tomatoes',
        'prep_time' : 'two hours',
        'created_at' : 'jan 13, 2023'
    },
     {
        'title': 'lasagne',
        'ingredients': 'mince meast, cheese, tomato sause',
        'prep_time' : 'one hour',
        'created_at' : 'jan 13, 2023'
    },
]

def home(request):
    context = {
        'cuisines' : cuisines
    }
    return render(request, 'cuisine/home.html', context)


def about(request):
    return render(request, 'cuisine/about.html')
