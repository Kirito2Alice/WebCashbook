'''cashbook app的 urls'''
from django.urls import path
from . import views
urlpatterns = [
    path('login', views.UsrLogin.as_view()),
]
