from django.urls import path
from .views import home # importuojame views



urlpatterns = [
    # import app urls
    path('', home, name="home"),

]
