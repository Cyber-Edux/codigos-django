from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'incorrect_login': False 
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/userspace')
        else:
            return render(request, 'login.html', {
                'incorrect_login': True 
            })
    else:
        return HttpResponseBadRequest()


@login_required(login_url='/login')
def userspace_view(request):
    return render(request, 'userspace.html', {
        'username': request.user.username
    })


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


def signup_view(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        login(request, user)
        return HttpResponseRedirect('/userspace')
    else:
        return HttpResponseBadRequest()