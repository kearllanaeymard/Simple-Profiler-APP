from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    queryset = User.objects.order_by('-id')
    context = {
        'nav_user'  :'active',
        'users': queryset
    }
    return render(request, 'users/index.html', context)

@login_required(login_url='/users/login')
@permission_required('users.add_user', login_url='/users/login')
def add(request):
    context = {
        'nav_add'   :'active',
    }
    return render(request, 'users/addnew.html', context)

def adduser(request):
    fname = request.POST['fname'].title()
    lname = request.POST['lname'].title()
    email = request.POST['email']
    position = request.POST['position'].title()
    if request.FILES.get('image'):
        profile_pic = request.FILES.get('image')
    else:
        profile_pic = 'profile_pic/default.jpg'

    try:
        context = {
            'nav_add'   :'active',
            'error_message' : 'Email Address has already been taken: ' + email,
        }
        n = User.objects.get(user_email = email) #If already exist
        return render(request, 'users/addnew.html', context)
    except ObjectDoesNotExist:
        context = {
            'nav_add'   :'active',
            'success_message' : 'User successfully created: ' + fname + ' ' + lname,
        }
        queryset = User.objects.create(
            user_fname = fname,
            user_lname = lname,
            user_email = email,
            user_position = position,
            user_img = profile_pic
        )
        return render(request, 'users/addnew.html', context)
    
@login_required(login_url='/users/login')
def detail(request, profile_id):
    queryset = User.objects.get(pk=profile_id)
    
    return render(request, 'users/detail.html', {'user_account' : queryset})

@login_required(login_url='/users/login')
def delete(request, profile_id):
    User.objects.filter(id=profile_id).delete()
    return HttpResponseRedirect('/users')

@login_required(login_url='/users/login')
@permission_required('users.change_user', login_url='/users/login')
def edit(request, profile_id):
    queryset = User.objects.get(pk=profile_id)
    
    return render(request, 'users/edit.html', {'user_account' : queryset})

def edituser(request, profile_id):
    queryset = User.objects.get(pk=profile_id)
    queryset.user_fname = request.POST['fname'].title()
    queryset.user_lname = request.POST['lname'].title()
    queryset.user_email = request.POST['email']
    queryset.user_position = request.POST['position'].title()
    if request.FILES.get('image'):
        queryset.user_img = request.FILES.get('image')
    
    try:
        queryset.save()
        return HttpResponseRedirect('/users')
        
    except IntegrityError:
        context = {
            'user' : queryset,
            'error_message' : 'Email Address has already been taken: ' + queryset.user_email
        }
        return render(request, 'users/edit.html', context)

def searchuser(request):
    searchval = request.GET['searchval']
    queryset = User.objects.filter(Q(user_fname__icontains=searchval) | Q(user_lname__icontains=searchval) | Q(user_position__icontains=searchval)).order_by('-id')

    context = {
        'nav_user'  :'active',
        'users': queryset
    }
    return render(request, 'users/index.html', context)

def loginview(request):
    context = {
        'nav_log'   :'active',
    }
    return render(request, 'users/login.html', context)

def loginuser(request): 
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/users')
    else:
        context = {
        'nav_log'   :'active',
        'login_failed_message' : 'Incorrect Username or Password!',
    }
        return render(request, 'users/login.html', context)


def logoutview(request):
    context = {
        'nav_log'   :'active',
    }
    logout(request)
    return render(request, 'users/login.html', context)