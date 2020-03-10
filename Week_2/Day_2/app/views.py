from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_ppl" : Person.objects.all(),
        "all_pets" : Pet.objects.all()
    }
    return render(request, "index.html", context)

def newPerson(request):
    Person.objects.create(first_name = request.POST['fn'],
                          last_name = request.POST['ln'],
                          email = request.POST['email'],
                          password = request.POST['password'])
    return redirect("/")

def newPet(request):
    user = Person.objects.get(id=request.POST['user'])
    Pet.objects.create(name=request.POST['name'],
                       animal_type = request.POST['type'],
                       user_adopted = user)
    return redirect("/")