from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.db import connection
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout



def signup_trigger(username):
    cursor = connection.cursor()
    user_trigger_qry = """INSERT INTO User_Info(user_id) VALUES ('"""+username+"""'); """
    cursor.execute(user_trigger_qry)


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1']
                            )
            login(request, new_user)
            username = request.user.username
            signup_trigger(username)
            return redirect("/search")
        else:
            print("The form was not valid")
            return render(request, "signup.html", {"form":form, "message":"The form was not correct; please retry signup"})
    else:
    	form = RegisterForm()
    return render(request, "signup.html", {"form":form })


def login_view(request):
    if request.method != "POST":
        return redirect('/accounts/login')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/search")
    else:
        # Return an 'invalid login' error message.
        return redirect('/accounts/login')


def logout_view(request):
    logout(request)
    form = RegisterForm()
    return render(request, "signup.html", {"form":form })