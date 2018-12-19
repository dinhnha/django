# views.py
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
        "email" : "ledinhnha@gmail.com",
        "name" : "Le, Nha D"
    }
    return render(request, "ourApp/index.html", context)