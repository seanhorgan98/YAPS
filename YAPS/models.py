from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User as BaseUser
from django.db.models.signals import post_save
from django.core.validators import *
import django.db.models.deletion
from datetime import timedelta




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

    
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=Category.max_val)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Podcast(models.Model):
    max_vals = 1000
    image = models.ImageField(upload_to='podcasts', null=True, blank=True, default='podcasts/default.png')
    title = models.CharField(max_length=Category.max_val)
    slug = models.SlugField(blank=True)

    #audio_file = models.FileField(upload_to='episode', blank=True, null=True)

    #publish_date = models.DateField(auto_now_add=True)
    url = models.URLField(default='')
    duration_mins = models.IntegerField(default=0)
    RSS_feed = models.URLField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=max_vals)

    is_favourite = models.BooleanField(default=False)

    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Podcast, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


 

        
class User(models.Model):
    user_name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    email = models.EmailField()
    twitter = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
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
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)

    # The additional attributes we wish to include
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the  __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.user_name

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        user_profile.save()
        
post_save.connect(create_profile, sender = User)
