# import form class from django
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import widgets
from .models import Menu



# FriendForm class for views
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ['seller']
        fields=['name', 'price', 'type']

        name = forms.CharField(max_length='512')
        price = forms.IntegerField()
        CHOICES=[('FOOD', 'FOOD'),
         ('DRINK','DRINK')]
        type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
        labels = {
            'name': _('Menu Name'),
            'price': _('Price of Menu'),
            'type': _('Type'),
        }
