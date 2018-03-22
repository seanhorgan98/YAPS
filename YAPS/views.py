from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from YAPS.models import Podcast
from YAPS.forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    

    return render(request, 'YAPS/index.html')

    

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user :
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'YAPS/login.html', {'error_message': 'Your account has been disabled'})
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'YAPS/login.html', {})

    
@login_required
def restricted(request):
        return HttpResponse("Since you're logged in, you can see this text!")       


def register(request):
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
               user = user_form.save()
               user.set_password(user.password)
               user.save()
               profile = profile_form.save(commit=False)
               profile.user = user
               if 'picture' in request.FILES:
                   profile.picture = request.FILES['picture']
               profile.save()
               registered = True
            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()
        return render(request,'YAPS/register.html',{'user_form': user_form, 'profile_form': profile_form,'registered': registered})

        
        
            
                
                
    
