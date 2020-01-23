from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^singin$', views.singin, name="singin"),
    url(r'^singup$', views.singup, name="singup"),
    url(r'^singinteacher$', views.singinteacher, name="singinteacher"),
    url(r'^singupteacher$', views.singupteacher, name="singupteacher"),
]
