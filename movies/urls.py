from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('form', views.movie_create, name = 'form'),
    path('details/<int:movie_id>', views.movie_details, name= 'details'),
    path('update/<int:movie_id>', views.update_movie, name= 'update'),
    path('delete/<int:movie_id>', views.delete_movie, name= 'delete'),
]