# views.py

from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Rediriger vers une page de votre choix après la déconnexion
    return redirect('home')  # Remplacez 'home' par l'URL vers la page où vous voulez rediriger après la déconnexion
