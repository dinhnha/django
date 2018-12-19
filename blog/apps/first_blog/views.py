from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Hello. Here is the first blog app!"
    return HttpResponse(response)

def new(request):
    form = "This is where the registration form is."
    return HttpResponse(form)

def create(request):
    return redirect('/.')

def show(request, number):
    response="This is the place holder for blog"+number+"."
    return HttpResponse(response)

def edit(request, number):
    response = "this is the placeholder to edit blog number " +number+"."
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/.')
# Create your views here.
