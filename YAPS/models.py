from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
##from YAPS import forms
# Create your models here.


class Category(models.Model):
    max_val = 128
    name = models.CharField(max_length=max_val, unique=True)
    
    slug = models.SlugField(unique=True,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Podcast(models.Model):
    max_vals = 1000
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=Category.max_val)
    slug = models.SlugField(blank=True)

    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=300, blank=True)
    url = models.URLField()
    description = models.CharField(max_length=max_vals)

    def __str__(self):
        return self.title

class Episode(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    show_notes = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='episode')
    duration = models.FloatField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    user_name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    email = models.EmailField()
    twitter = models.CharField(max_length=150)
    home_url = models.URLField()
    bio = models.TextField()
    last_login = models.DateTimeField(auto_now_add=True)


    def __str__(self):
            return self.user_name

    

class Comment(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    User_name = models.CharField(max_length=300)
    podcast_name = models.CharField(max_length=300)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment

    

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User Model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the  __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username


