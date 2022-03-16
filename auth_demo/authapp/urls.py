from django.urls import path

from . import views

urlpatterns = [
    path('', views.auth_login, name='authapp-login'),
    path('profile', views.profile, name='authapp-profile'),
]
