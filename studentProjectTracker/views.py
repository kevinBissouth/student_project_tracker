from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def login(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect("dashboard")
    else:
        return render(request, 'auth-login.html')
        HttpResponse("Here's the text of the web page.")


def dashboard(request):
    return render(request, 'index.html')


# def login(request):
#     return render(request, 'auth-login.html')

def register(request):
    return render(request, 'auth-register.html')

def forgot_password(request):
    return render(request, 'auth-forgot-password.html')


def reset_password(request):
    return render(request, 'auth-reset-password.html')

def subscribe(request):
    return render(request, 'subscribe.html')