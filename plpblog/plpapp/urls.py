from django.urls import path
from .import views

urlpatterns = [
    path('', views.plpapp, name='hello'),
    path('hello/', views.plpapp, name='hello'),
    path('contact/', views.contact, name='contact'),
]