from django import forms
from django.shortcuts import render, get_object_or_404,redirect
from . models import Customer, Order, Review, Book, Genre
from .forms import CustomerForm
# Create your views here.

def main(request):
    data={}
    return render(request, "main.html", context=data)

def signin(request):
    data={}
    f = CustomerForm(request.POST or None)
    data['form'] = f
    if f.is_valid():
        f.save()
        return redirect("main")
    return render(request, "signin.html", context=data)

def signup(request):
    data={}
    f = CustomerForm(request.POST or None)
    data['form'] = f
    if f.is_valid():
        f.save()
        return redirect("signin")
    return render(request, "signup.html", context=data)