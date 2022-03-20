from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

# functional view
def home(request):
    # use render function to load html files
    return render(request, 'index.html')

# class based views



