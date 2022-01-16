from django import forms
from django.shortcuts import render, get_object_or_404,redirect
from .models import Customer, Order, Review, Book, Genre
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

#book_G_views
def welcom(request):
    pass
    return render(request, "welcom.html")
def show_gtype(request):
    pass
    return render(request,"bookhome.html")
def science_book(request):
    pass
    return render(request,"science.html")
def learn_book(request):
    pass
    return render(request,"learn.html")
def history_book(request):
    pass
    return render(request,"history.html")
def cook_book(request):
    pass
    return render(request,"cook.html")
def art_book(request):
    pass
    return render(request,"art.html")

def search(request):
  data = {}
  #tt = request.GET["search"]
  #sbook = Book.objects.filter(title__contains=tt)
  #data['title'] = sbook
  return render(request, "search.html", context=data)
  