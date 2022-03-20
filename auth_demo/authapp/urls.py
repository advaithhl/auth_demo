from django.urls import path, include

from . import views

other_login_urls = [
    path('', views.auth_login, name='authapp-login'),
    path('standard/', views.standard_login, name='standard-login'),
    path('otp/', views.otp_login, name='otp-login'),
]

urlpatterns = [
    path('login/', include(other_login_urls)),
    path('logout/', views.auth_logout, name='authapp-logout'),
    path('', views.profile, name='authapp-profile'),
]
