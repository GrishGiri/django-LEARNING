from django.http import HttpResponse  # Corrected import
from django.shortcuts import render 

def homepage(request):
    dd={
        'tt':'De Beauty Bar'
    }
    return render(request,"index.html",dd)

def aboutus(request):
    return render( request,"about.html")

def services(request):
    return render( request,"services.html")

def package(request):
    return render( request,"package.html")

def gallery(request):
    return render( request,"galery.html")

def Book(request):
    return render( request,"book.html")

def contact(request):
    return render( request,"contact.html")

def testimonials(request):
    return render( request,"testimonials.html")

