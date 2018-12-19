from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "Hello, Django is a little Crazy!"
    return HttpResponse(response)
