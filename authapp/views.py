from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect

def index(request):
    return render_to_response('index.html', {},
                              context_instance=RequestContext(request))

def register(request):
    return render_to_response('register.html', {},
                              context_instance=RequestContext(request))

def create_user(request):
    user_id = request.POST['user_id']
    password = request.POST['password']

    new_user = User.objects.create_user(user_id, None, password)
    new_user.save()

    return redirect('/')

def login(request):
    user_id = request.POST['user_id']
    password = request.POST['password']
    user = authenticate(username=user_id, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('/home')
        else:
            return redirect('/')
    else:
        return redirect('/')

def home(request):
    return render_to_response('home.html', {})