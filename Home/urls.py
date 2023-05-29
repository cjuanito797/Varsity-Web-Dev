from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'Home'

urlpatterns = [

    path('', views.home, name="home"),
    path('our_work/', views.our_work, name="our_work"),
    path('project_details/<int:pk>', views.project_details, name="project_details"),
]
