from django import forms
from django.forms import ModelForm
from .models import Contactform

class ContactformForm(forms.Form):
    customer_email = forms.EmailField(label='Correo electrónico')
    customer_name = forms.CharField(max_length= 64,label='Nombre')
    subject = forms.CharField(max_length=255, label='Asunto')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    class Meta:
        model = Contactform
        fields = ['customer_email', 'customer_name', 'subject', 'message']