from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .forms import UniversityForm


def index(request):
    context = {'form': UniversityForm()}
    return render(request, 'index.html', context)