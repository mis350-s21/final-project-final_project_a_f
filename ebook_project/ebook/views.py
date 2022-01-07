from django.shortcuts import render, get_object_or_404
from . models import Customer, Order, Review, Book, Genre
# Create your views here.

def main(request):
    data={}
    return render(request, "main.html", context=data)