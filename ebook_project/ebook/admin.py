from django.contrib import admin
from .models import Book,Genre
from .models import Customer, Order, Review
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
  pass

class OrderAdmin(admin.ModelAdmin):
  pass

class ReviewAdmin(admin.ModelAdmin):
  pass

class BookAdmin(admin.ModelAdmin):
  pass
class GenreAdmin(admin.ModelAdmin):
  pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre,GenreAdmin)