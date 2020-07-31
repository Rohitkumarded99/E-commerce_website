from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        phone = request.POST['phone']

        # check for error input
        if len(username) > 10:
            messages.error(request, "user name must be under10 character")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, "username must only contain name & number")
            return redirect('index')

        if pass1 != pass2:
            messages.error(request, "pasword do not match")
            return redirect('index')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.phone = phone
        myuser.save()
        messages.success(request, "your account has successfully created")
        messages.success(request, "Login Now !!")
        return redirect('index')

    else:
        return HttpResponse('not allowed')


def handleLogin(request):
    if request.method == 'POST':
        # get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged In ")
            return redirect('/shop')
        else:
            messages.error(request, " invalid login")
            return redirect('index')
    return HttpResponse('not allowed')


def handleLogout(request):
    logout(request)
    messages.success(request, "successfully logged out ")
    thank = True
    return redirect('index')