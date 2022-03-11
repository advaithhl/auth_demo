from django.shortcuts import render


def login(request):
    return render(request, 'authapp/login.html')

def profile(request):
    return render(request, 'authapp/profile.html')
