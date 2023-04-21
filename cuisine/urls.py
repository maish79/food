from django.urls import path
from . import views



urlpatterns = [
    path('', views.CuisineListView.as_view(), name='home'),
    path('cuisine/<int:pk>', views.CuisineDetailView.as_view(), name='cuisine-detail'),
    path('cuisine/create', views.CuisineCreateView.as_view(), name='cuisine-create'),
    path('about/', views.about, name='about'),
   
]