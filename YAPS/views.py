from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from YAPS.forms import UserForm, UserProfileForm, UserProfile, PodcastForm, MyRegistrationForm, contactForm
from django.http import HttpResponse
from YAPS.models import Podcast,Category,User,UserProfile,Comment 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import auth
from django.core.mail import send_mail, BadHeaderError
from django.template import RequestContext
import os
from YAPS.models import Podcast
from django.shortcuts import get_object_or_404



def index(request):
    podcast_list=Podcast.objects.all().order_by('publish_date')
    visitor_cookie_handler(request)

    return render(request, 'YAPS/index.html', {'podcast_list': podcast_list})


def category(request):
    
    return render(request, 'YAPS/category.html', {})
def add_podcast(request, category_name_slug):

    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PodcastForm()

    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            if category:
                podcast = form.save(commit=False)
                podcast.category = category
                podcast.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'YAPS/add_podcast.html', context_dict)

def show_podcast(request, category_name_slug, podcast_name_slug):
    podcast = Podcast.objects.get(slug=podcast_name_slug)
    context_dict = {}
    context_dict['podcast'] = podcast



    response = render(request, 'YAPS/podcast.html', context_dict)

    return response

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        podcasts = Podcast.objects.filter(category=category)

        context_dict['podcasts'] = podcasts
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['podcasts'] = None

    return  render(request, 'YAPS/category.html', context_dict)

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
            return render(request, 'YAPS/login.html', {'error_message': 'Invalid login details'})
    else:
        return render(request, 'YAPS/login.html', {})

    
@login_required
def restricted(request):
        return HttpResponse("Since you're logged in, you can see this text!")       


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)    # create form object
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
        
     
    return render(request, 'YAPS/register.html', {'user_form': user_form,'profile_form': profile_form,'registered': registered})
        
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val



def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits
    
    
def profile(request):
    registered = True
    return render(request, 'YAPS/profile.html', {}) 


def about(request):
    return render(request, 'YAPS/about.html', {})

def contact(request):
    
    if request.method == 'GET':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['seanhorgan98@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
    
    return render(request, 'YAPS/contact.html', {'form': form})


                
    
