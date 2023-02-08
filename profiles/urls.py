from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order-history', views.profile, name='profile')
]
