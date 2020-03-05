from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def hello(request):
    return HttpResponse("hey again")

def hello_with_name(request, name):
    return HttpResponse(f"Hey there {name}")

def returnHTML(request):
    age = 26
    hobbies = ["tea","cats","coding"]
    context = {
        "fn" :"Nadia",
        "age" : age,
        "hobbies" : hobbies
    }
    return render(request, "index.html", context)