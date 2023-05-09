from django.urls import path

from .import views


 
urlpatterns = [
    path('', views.CuisineListView.as_view(), name='home'),
    path('cuisine/<int:pk>', views.CuisineDetailView.as_view(), name='cuisine-detail'),
    path('cuisine/create', views.CuisineCreateView.as_view(), name='cuisine-create'),
    path('cuisine/<int:pk>/update/', views.CuisineUpdateView.as_view(), name='cuisine-update'),
    path('cuisine/<int:pk>/delete/', views.CuisineDeleteView.as_view(), name='cuisine-delete'),
    path('<int:cuisine_id>/add-comment/', views.add_comment, name='add-comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete-comment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
   
]


