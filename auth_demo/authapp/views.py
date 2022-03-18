from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def auth_login(request):
    if request.user.is_authenticated:
        return redirect('authapp-profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authapp-profile')
    else:
        return render(request, 'authapp/login.html')


@login_required
def auth_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'authapp/logout.html')


@login_required
def profile(request):
    return render(request, 'authapp/profile.html')
