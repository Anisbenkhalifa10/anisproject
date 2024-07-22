from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Debug: username={username}, password={password}")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')
        else:
            print("Debug: Authentication failed")
            return render(request, 'login.html', {'error': 'Invalid credentials or insufficient permissions'})

    return render(request, 'login.html')
