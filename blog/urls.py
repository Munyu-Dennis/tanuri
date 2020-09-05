from django.urls import path
from blog.views import BlogListView
from blog.views import blogdetail
from django.conf.urls import url
urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    url(r'^(?P<id>\d+)/$', blogdetail, name='blogdet')
]
