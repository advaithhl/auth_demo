from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login


def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authapp-profile')
    else:
        return render(request, 'authapp/login.html')

def profile(request):
    return render(request, 'authapp/profile.html')
