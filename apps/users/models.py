# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # check all fields for emptyness
        for field, value in post_data.items():
            if len(value) < 1:
                errors[field] = "{} field is reqired".format(field.replace('_', ' '))

            # check name fields for min length
            if field == "first_name" or field == "last_name":
                if not field in errors and len(value) < 3:
                    errors[field] = "{} field must bet at least 3 characters".format(field.replace('_', ' '))

            # check password field for valid password
            if field == "password":
                if len(post_data['password']) < 8:
                    errors[field] = "{} Password must be at least 8 characters".format(field.replace('_', ' '))

                if not post_data['password'] == post_data['confirmpass']:
                    errors[field] = "{} Password doesn't match".format(field.replace('_', ' '))


        # check email field for valid email
        if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "invalid email"

        # if email is valid check db for existing email
        else:
            if len(self.filter(email=post_data['email'])) > 1:
                errors['email'] = "email already in use"

        return errors

        def validate_log(self, post_data):
            errors = {}
            current_user = User.objects.filter(email=post_data["email"])
            print (User.objects.filter(email=post_data["email"]))
            if not current_user:
                errors.appends(['accounts', "Email or password is incorrect"])
            elif not bcrypt.checkpw(post_data['password'].encode(), current_user[0].hashpw.encode()):
                errors.appends(['accounts', "Email or password incorrect"])
            if errors:
                return [False, errors]
            else:
                return [True, current_user[0]]

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hashpw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


    # def __str__(self):
    #     return self.email
