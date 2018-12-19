from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey_app/index.html')

def success(request):
    return render(request, "survey_app/success.html")

def process(request):
    print(request.POST)
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/success')
# Create your views here.
