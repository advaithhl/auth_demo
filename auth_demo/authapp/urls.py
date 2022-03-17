from django.urls import path

from . import views

urlpatterns = [
    path('', views.auth_login, name='authapp-login'),
    path('logout', views.auth_logout, name='authapp-logout'),
    path('profile', views.profile, name='authapp-profile'),
]
