from django.db import models
from django.template.defaultfilters import slugify

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=Category.max_val)
    slug = models.SlugField(blank=True)
    audio_file = models.FileField(upload_to='episode', blank=True, null=True)

    publish_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=300, blank=True)
    url = models.URLField(default='')
    description = models.CharField(max_length=max_vals)
    image = models.ImageField(upload_to='podcasts', null=True, blank=True, default='podcasts/default.png')
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
    twitter = models.CharField(max_length=150)
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
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the  __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username


