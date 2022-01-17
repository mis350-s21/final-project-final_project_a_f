from django.urls import path
from .import views
 
urlpatterns = [
    path('', views.main, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('cart/', views.cart, name='cart'),
    path('createbook/', views.create_book, name="create-book"),
    path('new_books_list/', views.new_books_list, name="new_books_list"),
    #book_G_views
    path('show/',views.show_gtype,name='show_gtype'),
    path('science/',views.science_book, name='science_book'),
    path('learn/',views.learn_book),
    path('history/',views.history_book),
    path('cook/',views.cook_book),
    path('art/',views.art_book),
    path('search/',views.search),
    path('search/<str:title>/',views.search_t,name='search-title'),
    path('type/<str:title>/',views.show_type),

]