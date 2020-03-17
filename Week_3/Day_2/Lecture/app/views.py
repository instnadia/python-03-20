from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def reg(request):
    errors = User.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    
    is_user_in_db = User.objects.filter(email = request.POST['email']).first() # if already existing will return an objects of a user

    if is_user_in_db:
        print("user is already exsiting")
        return redirect("/")
    
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user_created = User.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        email = request.POST['email'],
        password = hashed_pw
    )

    request.session['user_id'] = user_created.id

    return redirect('/success')

def success(request):
    user_id_is_session = request.session.get('user_id')
    if user_id_is_session:
        user_from_db = User.objects.get(id = user_id_is_session)
        context = {
            "user": user_from_db,
            "all_messages": Message.objects.all().order_by("-created_by")
        }
        return render(request, "success.html", context)
    return redirect("/")

def log(request):
    found_user = User.objects.filter(email = request.POST['email']).first()

    if found_user: # if email is found in db
        is_pw_correct = bcrypt.checkpw(
            request.POST['password'].encode(),
            found_user.password.encode()
        )

        if is_pw_correct: # if password is correct
            request.session['user_id'] = found_user.id
            return redirect('/success')
        else: #if pw is incorrect
            print("something is not working")
            return redirect("/")
    else: # if email is not found
        print("something is not working")
        return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

def new_message(request):
    errors = Message.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/success")

    user_id = request.session.get("user_id")
    user_from_db = User.objects.get(id = user_id)

    Message.objects.create(
        message = request.POST['message'],
        created_by = user_from_db
    )

    return redirect("/success")

def new_comment(request, id):
    # validate your comment in here!!!!!

    # errors = Message.objects.validator(request.POST)

    # if len(errors)>0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect("/success")

    user_id = request.session.get("user_id")
    user_from_db = User.objects.get(id = user_id)

    message_commented_on = Message.objects.get(id = id)

    Comments.objects.create(
        comment = request.POST['comment'],
        created_by = user_from_db,
        commented_at = message_commented_on
    )

    return redirect("/success")