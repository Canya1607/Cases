from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', views.login, name='login'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]