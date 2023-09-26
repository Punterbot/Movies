from django.shortcuts import render
from .models import Movie
import json

def movie_list(request):
    movies = Movie.objects.all()
    #json_data = open('/static/index.json')
    with open('C:\Final_Project\movies\json\index.json', 'r') as json_file:
        data = json.load(json_file)   
    # Process the movies array
    #get uniq Genre
    all_genre=set()
    for i in data:
        movies = i.get("movies", [])
        for movie in movies:
            genre = movie.get("genre", "")
            for g in genre:
                all_genre.add(g)    
        
    return render(request, 'movies/movie_list.html', {'movies_list': data,'all_genre':all_genre})

# Below Functin i didnt use as all requirements were fullfilled without using separate function 
def filter_movies(request):
    genre = request.GET.get('genre')
    movies = Movie.objects.filter(genre__icontains=genre)
    return render(request, 'movies/movie_list.html', {'movies': movies})