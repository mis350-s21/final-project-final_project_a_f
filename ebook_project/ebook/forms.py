from django import forms
from .models import Customer,Book

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"