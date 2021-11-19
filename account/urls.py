from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.create_user, name= 'signup')
]