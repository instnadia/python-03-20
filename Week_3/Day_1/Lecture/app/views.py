from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0 :
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/")
    
    is_in_db = User.objects.filter(email = request.POST['email']).first()
    if is_in_db:
        print('email already registered')
        return redirect("/")
    hashed_password = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()
    
    new_user = User.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        email = request.POST['email'],
        password = hashed_password
    )

    request.session['user_id'] = new_user.id

    return redirect('/success')

def success(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.error(request, 'Try to login/register')
        return redirect('/')
    else:
        user_from_db = User.objects.get(id = user_id)
        context = {
            "user": user_from_db,
            "good_boyz" : Dog.objects.filter(is_good_boy = True),
            "bad_boyz" : Dog.objects.filter(is_good_boy = False),
            "dogs_by_user" : Dog.objects.filter(submitted_by = user_from_db)
        }
        return render(request, 'dash.html', context)
    
def login(request):
    found_user = User.objects.filter(email=request.POST['email'])
    if len(found_user)>0:
        user_from_db = found_user[0]

        is_pw_correct = bcrypt.checkpw(
            request.POST['password'].encode(),
            user_from_db.password.encode()
        )

        if is_pw_correct:
            request.session['user_id'] = user_from_db.id
            return redirect('/success')
        else:
            print('password is incorect')
    else:
        print('no user found')

    messages.error(request, 'Invalid cradential')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def create_dog(request):
    context = {
        "tricks" : Trick.objects.all()
    }
    return render(request, "new_dog.html", context)

def add_dog(request):
    errors = Dog.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/dog/new")
    
    user_id = request.session.get("user_id") # getting user's Id in session

    user_created = User.objects.get(id = user_id) # searching user in DB by Id that was storred in session

    new_dog = Dog.objects.create(
        name= request.POST['name'],
        profile_pic_url = request.POST['profile_pic'],
        bio = request.POST['bio'],
        age = request.POST['age'],
        birthday = request.POST['bday'],
        weight = request.POST['weight'],
        submitted_by = user_created
    )

    checkbox = request.POST.getlist('trick') # grabs all the values that were checked with the name "trick"

    if checkbox is not None: # if there are tricks selected
        print("$"*100)
        print(checkbox)
        for trick in checkbox:
            trick_from_db = Trick.objects.get(id = trick) # get it from the db
            new_dog.tricks.add(trick_from_db) # assign it to a dog
    
    other_trick = request.POST['trick_other'] # the other field

    if other_trick!="":
        other_trick = other_trick.lower().capitalize()

        trick_from_db = Trick.objects.filter(name = other_trick).first() # check if already in db

        if trick_from_db == None:
            new_trick = Trick.objects.create(name=other_trick) # if not in db, create it
        
        new_dog.tricks.add(new_trick) # assign it to the dog
    
    return redirect("/success")

def toggle(request, id):
    dog_from_db = Dog.objects.get(id=id) # getting the dog from db based on id from the url

    dog_from_db.is_good_boy = not dog_from_db.is_good_boy # setting the other bool value to itsef
    dog_from_db.save() # SAVE!!!!!
    return redirect("/success")

def edit(request, id):
    dog_from_db = Dog.objects.get(id=id) # getting dog from db by the id provided from the path

    context = {
        "dog":dog_from_db
    }
    return render(request, "edit.html", context)

def update(request, id):
    errors = Dog.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/dog/{id}/edit")
    
    dog_from_db = Dog.objects.get(id = id)

    dog_from_db.name = request.POST['name']
    dog_from_db.profile_pic_url = request.POST['profile_pic']
    dog_from_db.bio = request.POST['bio']
    dog_from_db.age = request.POST['age']
    dog_from_db.weight = request.POST['weight']
    dog_from_db.birthday = request.POST['bday']

    dog_from_db.save()

    return redirect(f"/dogs/{id}")

def one_dog(request, id):
    dog_from_db = Dog.objects.get(id=id)
    context = {
        "dog":dog_from_db
    }

    return render(request, "one_dog.html", context)

def delete(request, id):
    dog_from_db = Dog.objects.get(id=id)

    dog_from_db.delete()
    return redirect("/success")
