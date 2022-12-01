from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Menu
from .forms import MenuForm

# imported login required
from django.contrib.auth.decorators import login_required

# For each, added login required so must be logged in as admin
@login_required(login_url='/admin/login/')
def index(request):
    menu = Menu.objects.filter(seller=request.seller)
    response = {'menu': menu, 'seller': request.seller}
    return render(request, 'menu_index.html', response)

@login_required(login_url='/admin/login/')
def add_menu(request):
  
    # create object of form
    form = MenuForm(request.POST or None)
      
    # check if form data is valid
    if (form.is_valid() and request.method == 'POST'):
        # save the form data to model
        form.seller = request.seller
        form.save()
        # when saved go back to menuapp
        return HttpResponseRedirect('/menu')
    
    else:
        form = MenuForm()

    response = {'form' : form}
    return render(request, 'menu_form.html', response)
