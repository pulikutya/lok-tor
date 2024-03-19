from django.shortcuts import render
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.

def view_bejelentkezés(request):
    return render(request,"bejelentkezés.html",{})


def view_regisztráció(request):
    return render(request,"regisztráció.html",{})

def view_regisztráció_küld(request):
    if(request.POST["jelszó"]!=request.POST["jelszó2"]):
        return render(request)
    user = User.objects.create_user(request.POST["felhasználónév"])
    return render(request,)