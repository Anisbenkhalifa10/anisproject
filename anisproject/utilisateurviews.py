from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from anisproject.utilisateurforms import UtilisateurForm
from anisproject.utilisateurmodes import Utilisateur

@login_required
def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'utilisateur/liste_utilisateur.html', {'utilisateurs': utilisateurs})
@login_required
def ajouter_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_utilisateurs')
    else:
        form = UtilisateurForm()
    return render(request, 'utilisateur/ajouter_utilisateur.html', {'form': form})
@login_required
def modifier_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    if request.method == 'POST':
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('liste_utilisateurs')
    else:
        form = UtilisateurForm(instance=utilisateur)
    return render(request, 'utilisateur/modifier_utilisateur.html', {'form': form})

def supprimer_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    if request.method == 'POST':
        utilisateur.delete()
        return redirect('liste_utilisateurs')
    return render(request, 'utilisateur/supprimer_utilisateur.html', {'utilisateur': utilisateur})