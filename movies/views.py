from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm

def index(request):
    m_context={
        'movies':movie.objects.all()
    }
    return render(request, 'movies/index.html', context= m_context)

def movie_create(request):
    form = MovieForm()
    if request.method=="POST" :
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    return render(request, "movies/create_form.html", context={'form':form})

def movie_details(request, movie_id):
    element = movie.objects.get(pk=movie_id)
    return render(request, "movies/details.html", context={'movie': element})

def update_movie(request, movie_id):
    element = movie.objects.get(pk=movie_id)
    if request.method == "POST":
        form = MovieForm(data=request.POST, instance=element)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=element)
        m_context = {'form': form,
                     'movie_id': movie_id}
        return render(request, "movies/update_form.html", context=m_context)

def delete_movie(request, movie_id):
    movie.objects.get(pk=movie_id).delete()
    return redirect('movies:index')