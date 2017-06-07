from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='irb-sterowanie'),
    url(r'^blog/$', views.blog, name='blog'),
]
