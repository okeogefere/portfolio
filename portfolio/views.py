from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Contacted Oke Ogefere')
            return redirect('home')
        else:
            print("form not submitted successfully", form.errors)
        
    else:
        form = ContactForm()
        print("form re rendering")
    return render(request, 'portfolio/index.html', {'form': form})