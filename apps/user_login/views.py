from django.shortcuts import render, HttpResponse, redirect
from apps.user_login.models import *
# Create your views here.
def userindex(request):
    context = {
        "users": User.objects.all(),
    }
    return render(request, 'user_login/index.html', context)
