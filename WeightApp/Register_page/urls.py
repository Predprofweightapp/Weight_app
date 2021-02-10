from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.auth, name='auth'),
    path('reg/', views.reg, name='reg'),
    path('profile/', views.profile, name='profile'),
]