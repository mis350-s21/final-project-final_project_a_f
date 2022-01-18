
from django.shortcuts import render, get_object_or_404,redirect
from .models import Book,Customer, Order, Review, Genre
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

def cook_book(request):
    pass
    return render(request,"cook.html")
def art_book(request):
    pass
    return render(request,"art.html")

def search(request):
  data = {} 
  book = Book.objects.all()
  data['title'] = book
  return render(request, "search.html", context=data)

def search_t(request,title):
  data = {} 
  title = request.GET["title"]
  sbook = Book.objects.filter(title__icontains=title)
  data['title_s'] = sbook
  return render(request, "search_t.html", context=data)

def show_type(request,title):
    data={}
    book=Book.objects.filter(title=title)
    gener=Genre.objects.filter(type__contains=book)
    data['title_s'] = book
    data['type'] = gener
    return render(request, "show_type.html", context=data)

def history_book(request):
    pass
    return render(request,"history.html")
def add_cart(request):
    data={}
    return render(request, "history.html", context=data)


def del_cart(request):
    data={}
    return render(request, ".html", context=data)
def upd_cart(request):
    data={}
    return render(request, ".html", context=data)
def details_cart(request):
    data={}
    return render(request, "cart_det.html", context=data)