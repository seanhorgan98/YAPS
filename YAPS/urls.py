from django.conf.urls import url
from YAPS import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_podcast/$', views.add_podcast, name='add_podcast'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<podcast_name_slug>[\w\-]+)/$', views.show_podcast, name='show_podcast'),

    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^restricted/', views.restricted, name='restricted'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




