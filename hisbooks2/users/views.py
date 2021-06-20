from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# def signup(request):
#     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#     # At this point, user is a User object that has already been saved
#     # to the database. You can continue to change its attributes
#     # if you want to change other fields.
#     user.last_name = 'Lennon'
#     user.save()



# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
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
