from django.urls import path
from .import views
 
urlpatterns = [
    path('', views.main, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    #book_G_views
    path('show/',views.show_gtype,name='show_gtype'),
    path('science/',views.science_book, name='science_book'),
    path('learn/',views.learn_book),
    path('history/',views.history_book),
    path('cook/',views.cook_book),
    path('art/',views.art_book),
    path('search/',views.search),

]