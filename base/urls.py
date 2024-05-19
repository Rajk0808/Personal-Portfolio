
from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name = "home"),
    path("achivements", views.achivements , name = "achivements"),
    path("contact" , views.contact , name = "contact"),
    path("about" , views.about , name = "about"),
    path("projects" , views.projects , name = "projects")
]
