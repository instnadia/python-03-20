from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_s": Student.objects.all()
    }
    return render(request, "index.html", context)

def add_s(request):
    Student.objects.create(name=request.POST["name"], grade=request.POST['grade'])
    return redirect("/")

def display_teachers(request):
    context = {
        "all_t": Teacher.objects.all()
    }
    return render(request, "teacher.html", context)

def add_t(request):
    Teacher.objects.create(name=request.POST['name'], subject=request.POST['subject'])
    return redirect("/teachers")

def show_s(request,id):
    s = Student.objects.filter(id=id) # filter is safer because if id doesnt exsit will return empty dictionary
    context = {
        "student": s
    }

    return render(request, "student.html", context)
