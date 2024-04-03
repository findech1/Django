from django.urls import path
from .import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('hello/', views.hello, name='hello'),
    path('contact/', views.contact, name='contact'),
]