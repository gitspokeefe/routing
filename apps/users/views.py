# 1. On error registration form needs to remain on registration form
# 2. On error login form needs to remain on registration form
# 3. Uniquie email address fail needs to have error message


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, "users/create.html")


def registration(request):
    return render(request, "users/registration.html")
    if len(errors):
        for field, message in errors.items():
            error(request, message, extra_tags=field)

        return redirect('users/registration')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.items():
            error(request, message, extra_tags=field)

        return redirect('/users/new')

    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
    )
    return redirect('/users')


def login(request):

    return render(request, 'users/', context)

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'users/update.html', context)

def update(request, user_id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.items():
            error(request, message, extra_tags=field)

        return redirect('/users/{}/edit'.format(user_id))

    user_to_update = User.objects.get(id=user_id)
    user_to_update.first_name = request.POST['first_name']
    user_to_update.last_name = request.POST['last_name']
    user_to_update.email = request.POST['email']
    user_to_update.save()
    return redirect('/users')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'users/show.html', context)


def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')
