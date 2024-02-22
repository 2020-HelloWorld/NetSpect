from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import models


# Create your views here.
@csrf_exempt
def login_api(request):
    if request.method == "POST":
        print(request.POST)
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "login_page.html")
        except Exception as e:
            print("Login error:", e)
            return render(request, "login_page.html")
    else:
        return render(request, "login_page.html")


@login_required(login_url="/login/")
def logout_api(request):
    logout(request)
    return redirect("/login/")
