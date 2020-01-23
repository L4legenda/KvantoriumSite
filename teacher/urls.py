from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^account$', views.account, name="account"),
    url(r'^groups$', views.groups, name="groups"),
    url(r'^students$', views.students, name="students"),
    url(r'^timetable$', views.timetable, name="timetable"),
]
