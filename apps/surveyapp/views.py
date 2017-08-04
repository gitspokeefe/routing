from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "this is a placeholder for SURVEY"
    return HttpResponse(response)
