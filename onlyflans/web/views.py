from django.shortcuts import render
from .models import Flan, Contactform
from django.http import HttpResponseRedirect
from .forms import ContactformForm, ContactFormModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def indice(request):
    public_flans = Flan.objects.filter(is_private= False)
    return render(request,'index.html',
                  {
                      'public_flans': public_flans
                  })

def acerca(request):
    return render(request,'about.html',{})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request,'welcome.html',{
        'private_flans': private_flans
    })
    
def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        
        if form.is_valid():
            
            contact_form = Contactform.objects.create(**form.cleaned_data)
            
            return HttpResponseRedirect('/exito')
    else:
        form = ContactformForm()
            
    return render(request,'contacto.html',{'form' :form})

def exito(request):
    return render(request,'success.html',{})

"""
def recetas(request):
    recetas = Recetas.objects.all()
    return render(request,'recetas.html',{
        'recetas': recetas
    })
"""
