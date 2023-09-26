from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('filter/', views.filter_movies, name='filter_movies'),
]