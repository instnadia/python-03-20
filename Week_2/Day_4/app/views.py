from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "index.html")

#responsible for POST request in form submission and validation
def submit(request):
    # validator is coming from the UserManager class, it is a function
    errors = User.objects.validator(request.POST)

    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.create(first_name=request.POST['first_name'],
                            last_name = request.POST['last_name'],
                            email = request.POST['email'],
                            birth_day = request.POST['birth_day'],
                            password = request.POST['password'])
        request.session['user_id'] = user.id #session to keep the user's id
        return redirect("/success")

def success(request):
    user_id = request.session.get('user_id')
    if user_id != None:
        context = {
            "user" : User.objects.get(id=user_id)
        }
        return render(request, 'success.html', context)
    else:
        return redirect("/")