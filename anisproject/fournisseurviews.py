from django.contrib.auth.decorators import login_required

from .fournisseurmodels import Fournisseur

@login_required
def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'Fournisseur/liste_fournisseurs.html', {'fournisseurs': fournisseurs})


# Dans fournisseur/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .fournisseurforms  import FournisseurForm

@login_required
def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm()

    return render(request, 'Fournisseur/ajouter_fournisseur.html', {'form': form})


@login_required
def supprimer_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)

    if request.method == 'POST':
        fournisseur.delete()
        return redirect('liste_fournisseurs')

    return render(request, 'Fournisseur/supprimer_fournisseur.html', {'fournisseur': fournisseur})

@login_required
def modifier_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)

    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)

    return render(request, 'Fournisseur/modifier_fournisseur.html', {'form': form, 'fournisseurs': fournisseur})