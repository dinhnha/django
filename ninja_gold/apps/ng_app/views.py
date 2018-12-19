from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render( request, 'ng_app/index.html')

def process_money(request):
    return redirect('/')