from django.shortcuts import render
from first.forms import SelectionForm

#Create your views here.

def index(request):
    return render(request, 'reviews/index.html')

def drone(request):

    return render(request, 'reviews/articles/drone.html')
