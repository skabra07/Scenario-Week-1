from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Log
from .forms import LoginForm,SignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    username = ''
    password = ''
    fname = ''
    lname = ''
    if request.method == 'POST':
        if 'login' in request.POST:
            login = LoginForm(request.POST)
            signup = SignUpForm()
            if login.is_valid():
                username = login.cleaned_data['username']
                password = login.cleaned_data['password']
            else:
                login = LoginForm()                
                return render(request,'index.html',{"login":login,"signup":signup})

            login = LoginForm() 
            try:
                checkUser = User.objects.get(username=username)
            except User.DoesNotExist:
                return render(request,'index.html',{"login":login,"signup":signup})

            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('homepage')
            else:
                return render(request,'index.html',{"login":login,"signup":signup})

        elif 'signup' in request.POST:
            login = LoginForm()
            signup = SignUpForm(request.POST)
            if signup.is_valid():
                 username = signup.cleaned_data['username']
                 password = signup.cleaned_data['password']
                 fname = signup.cleaned_data['fname']
                 lname = signup.cleaned_data['lname']
            else:
                signup = SignUpForm()                
                return render(request,'index.html',{"login":login,"signup":signup})
            
            try:
                print("in signup")
                user = User.objects.create_user(username = username,password = password,first_name = fname,last_name = lname)
                user.save()
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request,user)
                    return redirect('homepage')
            except Exception:
                print("error")
                signup = SignUpForm()                
                return render(request,'index.html',{"login":login,"signup":signup})
    else:
        login = LoginForm()
        signup = SignUpForm()
        return render(request,'index.html',{"login":login,"signup":signup})

@login_required 
def homepage(request):    
    logsQuery = Log.objects.all() 
    logs = []
    for log in logsQuery[::-1]:
        userObject = User.objects.get(username=log.username)
        username = userObject.get_full_name()
        id = log.id
        createdTime = log.createdTime
        description = log.description
        res = {'username':username,'createdTime':createdTime,'description':description,'id':id}
        logs.append(res) 
    return render(request,'homepage.html',{
        'logs':logs,
    })

@login_required
def add(request):
    if request.method == "POST":
        user = request.user
        logText = request.POST.get('log')
        print(request.POST)
        log = Log(description = logText,username=user)
        log.save()
    return redirect(homepage)

@login_required 
def delete(request,id):
    log = Log.objects.get(id=id)
    log.delete()
    return redirect('homepage')

@login_required 
def edit(request,id):
    if request.method == "POST" and request.POST.get('log') :
        log = Log.objects.get(id=id)
        log.description = request.POST.get('log')
        log.save()     
    return redirect('homepage')

@login_required 
def logout(request):
    auth_logout(request)
    return redirect('index')
    
