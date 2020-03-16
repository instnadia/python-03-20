from django.db import models
from django.contrib import messages
from datetime import datetime
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['fname'])<2:
            errors['fname'] = 'First name at least 2 characters'
        if len(data['lname'])<2:
            errors['lname'] = 'Last name at least 2 characters'
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = 'Email is invalid'
        if len(data['password'])<8:
            errors['password'] = 'Password must be at least 8 characters'
        if data['password']!=data['cpassword']:
            errors['cpassword'] = 'Passwords much match'
        
        return errors
    
    def LogValidator(self,data):
        pass

class DogManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['name'])<2:
            errors['name'] = "Name cannot be shorter than 2 characters"
        if data['profile_pic']=="":
            errors["profile_pic"] = "Profile picture cannot be empty"
        if data['bday']=="":
            errors['bday'] = 'Birthdate cnnot be empty'
        else:
            if datetime.strptime(data['bday'], '%Y-%M-%d') > datetime.today():
                errors['bday'] = "No days in the future"
        if data['age']=="":
            errors['age'] = 'Age is required'
        if data['bio']=="":
            errors['bio'] = 'Bio is required'
        if data['weight']=="":
            errors['weight'] = 'Weight is required'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trick(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Dog(models.Model):
    name = models.CharField(max_length=60)
    profile_pic_url = models.TextField()
    bio = models.TextField()
    age = models.IntegerField()
    weight = models.IntegerField()
    is_good_boy = models.BooleanField(default=False)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DogManager()

    submitted_by = models.ForeignKey(User, related_name = "dogs", on_delete=models.CASCADE)

    tricks = models.ManyToManyField(Trick, related_name="dogs_with_trick")

