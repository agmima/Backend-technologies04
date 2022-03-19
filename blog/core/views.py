from django.shortcuts import render
from django.http import HttpResponse

# functional view


def home(request):
    # use render function to load html files
    return render(request, 'index.html')
