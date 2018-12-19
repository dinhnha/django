from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "randstr" : get_random_string(length=14),
        "name" : "Le, Nha D"
    }
    return render(request, "randomword/index.html", context)

def reset(request):
    context = {
        "randstr" : get_random_string(length=14),
        "name" : "Le, Nha D"
    }
    return render(request, "randomword/index.html", context)
# Create your views here.
