from django.http import HttpResponse
from django.shortcuts import render

data =[ {
    'id':1,
    'name':'avatar',
    'date':'1-12-2010' },
    {'id':2,
    'name':'avengers',
    'date':'1-12-2010' },
    {'id':3,
    'name':'titanic',
    'date':'1-12-2010' }
]

def index(request):
    m_context={
        'movieslist':data
    }
    return render(request, 'todo/Index.html', context= m_context)

def movie_details(request, movie_id):
    movie = data[movie_id-1]
    print(movie)
    m_context = {
        'movie': movie
    }
    return  render(request, 'todo/movie_details.html', context = m_context)

def update_movie(request, movie_id):
    for i in range(len(data)):
        if data[i]['id'] == movie_id:
            data[i]['name'] = 'updated'
    m_context = {
        'movieslist': data
    }
    return render(request, 'todo/Index.html', context=m_context)

def delete_movie(request, movie_id):
    for i in range(len(data)):
        if data[i]['id'] == movie_id:
            del data[i]
            break
    m_context = {
        'movieslist': data
    }
    return render(request, 'todo/Index.html', context=m_context)
