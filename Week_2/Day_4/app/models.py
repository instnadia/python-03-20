from django.db import models
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['first_name'])<2:
            errors['first_name'] = "First name has to be at least 2 characters"
        if len(data['last_name'])<2:
            errors['last_name'] = "Last name has to be at least 2 characters"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Email is invalid"
        if data['birth_day']=='':
            errors['birthday'] = "Date cannot be empty"
        else:
            if datetime.strptime(data['birth_day'], '%Y-%m-%d')> datetime.today():
                errors['birthday'] = "Date cannot be in the future"
        if len(data['password'])<8:
            errors['password'] = "Password has to be at least 8 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    birth_day = models.DateTimeField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()