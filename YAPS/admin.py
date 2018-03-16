from django.contrib import admin
from YAPS.models import Category, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
##admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


