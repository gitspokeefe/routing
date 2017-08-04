from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
 # views.py

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "blogapp/index.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
