from django.conf.urls import url
from . import views

app_name = 'smallify'
urlpatterns = [

    url(r'^$', views.index, name="index" ),
    url(r'^detail/$',views.detail, name = "detail"),
    url(r'^redirect/(?P<compressed_url>.+)/$',views.redirect, name = "redirect"),
               
]