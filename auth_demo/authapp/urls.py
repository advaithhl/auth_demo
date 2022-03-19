from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.auth_login, name='authapp-login'),
    path('logout/', views.auth_logout, name='authapp-logout'),
    path('', views.profile, name='authapp-profile'),
]
