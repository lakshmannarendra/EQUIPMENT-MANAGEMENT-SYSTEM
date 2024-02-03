from django import forms
from .models import Borrow

class BorrowReturnForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['quantity']