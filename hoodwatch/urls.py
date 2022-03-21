from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('^$',views.index,name = 'index'),
    path('new/post$', views.new_post, name='newpost'),
    path('hoods', views.all_hoods, name='hoods'),
    path('business/',views.create_business,name = 'business'),
    path('profile/', views.profile, name='profile'),
    path('createHood/', views.createHood, name='createHood'),
    path('update/profile', views.updateprofile, name='updateprofile'),
    path('join/', views.join, name='joinHood'),
   path('search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)