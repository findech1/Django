from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('details/', views.details, name='details'),
]