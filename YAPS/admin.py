from django.contrib import admin
from YAPS.models import Category, Page, UserProfile, Comment, User, Podcast, Episode


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PodcastAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Episode)



