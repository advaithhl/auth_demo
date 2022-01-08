from django.shortcuts import render

def profile(request):
    return render(request, 'authapp/profile.html')
