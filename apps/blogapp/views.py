# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):

    return render(request, '/index.html', context)
