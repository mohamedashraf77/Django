from django.forms import ModelForm
from .models import movie

class MovieForm(ModelForm):

    class Meta:
        model = movie
        fields = '__all__'