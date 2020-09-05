from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('service/', views.service, name='service'),
    url(r'^(?P<id>\d+)/$', views.place_oder, name='place-oder'),
    path('about/', views.about, name='aboutus'),
    path('reviewform/', views.reviewform, name='reviewform'),
    path('contant/', views.contant, name='contant')
]
