from django.contrib import admin
from .models import Book,Genra

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  pass
class GenraAdmin(admin.ModelAdmin):
  pass
admin.site.register(Book, BookAdmin)
admin.site.register(Genra,GenraAdmin)