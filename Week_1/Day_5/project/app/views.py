from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'index.html')

def passLength(request):
    # print("#"*100)
    # print(request.POST['length_of_something'])
    request.session['length'] = request.POST['length_of_something']
    # print(request.session['length'])
    return redirect("/success")

def success(request):
    string_legnth = request.session.get('length') # getting the value from session using the key
    if string_legnth == None: # important! checking if the key is in session
        return redirect('/')
    unique_string = get_random_string(length=string_legnth)
    context = {
        "my_random_string" : unique_string
    }
    return render(request, 'success.html', context)