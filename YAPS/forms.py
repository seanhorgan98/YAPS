from django import forms
from YAPS.models import Category,Page, Podcast, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.max_val,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PodcastForm(forms.ModelForm):

    title = forms.CharField(max_length=Podcast.max_vals, help_text="Name")
    author = forms.CharField(max_length=Podcast.max_vals, help_text="Author")
    publish_date = forms.DateField(help_text="Publish Date")
    url = forms.URLField(help_text="Homepage URL")
    description = forms.CharField(max_length=Podcast.max_vals, help_text="Description")
    image = forms.ImageField(help_text="Podcast Image")

    class Meta:
        model = Podcast
        exclude = ('category','slug','audio_file')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
