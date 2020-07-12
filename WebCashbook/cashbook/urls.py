'''cashbook app的 urls'''
from django.urls import path
from . import views
urlpatterns = [
    path('login', views.AccountInfoView.as_view({'get': 'list'})),
]
