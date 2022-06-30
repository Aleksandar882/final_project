from email.mime import image
from email.policy import default
from django.shortcuts import render, redirect
from .models import Topic, Quiz, Badge
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.

from .forms import CreateUserForm

def index(request):
    return render(request, 'index.html')

def badges(request):
    queryset = Badge.objects.filter(user=request.user).all().filter(has_badge=True)
    context = {"badges": queryset, }
    return render(request, 'badges.html', context)

def topic1(request):
    queryset=Quiz.objects.filter(Question='VR typically incorporates')  
    context={"questions": queryset,}
    if 'option3' in request.POST:
        if Badge.objects.filter(name = "Intro Badge", user=request.user).exists():
            return redirect("topic1")
        else:
         badge = Badge(name="Intro Badge", user=request.user, has_badge=True)
         badge.save()
         currentuser=Badge.objects.get(user=request.user, name='Intro Badge')
         currentuser.save()
         return redirect("topic1")
    return render(request, 'topic1.html', context=context)

def topic2(request):
    queryset=Quiz.objects.filter(Question='What form of VR would be best for a Driving Simulator?')
    context={"questions": queryset,}
    if 'option2' in request.POST:
        if Badge.objects.filter(name = "Forms And Methods Badge", user=request.user).exists():
            return redirect("topic2")
        badge = Badge(name="Forms And Methods Badge", user=request.user, has_badge=True)
        badge.save()
        currentuser=Badge.objects.get(user=request.user, name='Forms And Methods Badge')
        currentuser.save()
        return redirect("topic2")
    return render(request, 'topic2.html', context=context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username Or Password is Incorrect')
        context={}
        return render(request, 'login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form= CreateUserForm()

        if request.method == 'POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        context={'form':form }
        return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def topics(request):
    queryset=Topic.objects.filter().all()
    context={"topics": queryset}
    return render(request, 'topics.html', context=context)