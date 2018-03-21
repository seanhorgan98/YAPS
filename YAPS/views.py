from django.shortcuts import render
from django.http import HttpResponse
from YAPS.models import Podcast
from YAPS.forms import UserForm,UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout



def index(request):
   
    response = render(request, 'YAPS/index.html')

    return response

def podcast(request):

    context_dict = {}





    response = render(request, 'YAPS/podcast.html')

    return response

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'YAPS/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                pods = Podcast.objects.filter(user=request.user)
                return render(request, 'YAPS/index.html', {'pods': pods})
            else:
                return render(request, 'YAPS/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'YAPS/login.html', {'error_message': 'Invalid login'})
    return render(request, 'YAPS/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                pods = Podcast.objects.filter(user=request.user)
                return render(request, 'YAPS/index.html', {'pods': pods})
    context = {
        "form": form,
    }
    return render(request, 'YAPS/register.html', context)
