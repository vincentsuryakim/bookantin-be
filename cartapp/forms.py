from django import forms
from .models import CartContent,Cart

class CartContentForm(forms.ModelForm):
    class Meta:
        model = CartContent
        fields = "__all__"

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"