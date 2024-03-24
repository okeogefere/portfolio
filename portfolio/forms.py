from django import forms 
from .models import *

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email','phone','message'] 
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Message', 'rows': 5}),
            }