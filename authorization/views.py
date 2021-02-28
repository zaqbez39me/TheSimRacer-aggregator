from django.contrib.admin import register
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages
from . import serializers

# Create your views here.

from authorization.forms import LoggingInForm, RegistrationForm
from .serializers import RegisterSerializer


def index(request):
    content = dict()
    content['user'] = request.user
    if request.method == "POST":
        post = request.POST
        if 'logout' in post:
            logout(request)
    return render(request, 'pages/index.html', content)


def log_in(request):
    content = dict()
    register()
    content['login_form'] = LoggingInForm()
    content['register_form'] = RegistrationForm()
    content['user'] = request.user
    if request.method == "POST":
        post = request.POST
        if 'logout' in post:
            logout(request)
        elif 'logging' in post:
            form = LoggingInForm(request.POST)
            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.WARNING, f'You logged in successfully {user}')
                content['authorized'] = True
                content['user'] = user
                content['login_form'] = form
            else:
                messages.add_message(request, messages.WARNING, f'Incorrect username or password')
        elif 'register' in post:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                username = form.data['username']
                if not User.objects.filter(username=username).exists():
                    serializer = RegisterSerializer.create(RegisterSerializer(), form.data)
                    for elem in form.data:
                        print(elem)
                    user = serializer.save()
                else:
                    messages.add_message(request, messages.ERROR, f'This username is already taken: {username}')
            else:
                for elem in form.data:
                    if len(form.data[elem]) == 0 and elem != 'register':
                        messages.add_message(request, messages.ERROR, f'The {elem} field is not correct')
            content['register_form'] = form
        content['request'] = request
        return render(request, 'pages/login.html', content)
    elif request.method == "GET":
        content['request'] = request
        return render(request, 'pages/login.html', content)
