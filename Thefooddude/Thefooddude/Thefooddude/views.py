from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return  render(request, 'Thefooddude/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register/')
            else:        
                user = User.objects.create_user(username = username, email = email, password = password1, )
                user.save()
                print("User Created")
                return redirect('/login/')

        else:
            messages.info(request, 'Password not matching')
            return redirect('/register/')
        return redirect('/')    

    else:   
        return render(request, 'Thefooddude/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/restaurant/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/login/')
    else:
        return render(request, 'Thefooddude/login.html')        


def logout(request):
    auth.logout(request)
    return redirect('/')
