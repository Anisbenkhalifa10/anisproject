from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .Forms import ProduitForm
from .models import Produit
@login_required
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'liste_produits.html', {'produits': produits})
# Vue pour ajouter un produit

@login_required
def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'supprimer_produit.html', {'produit': produit})
@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Enregistre directement le produit avec l'image téléchargée
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'ajouter_produit.html', {'form': form})
@login_required
def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)

    return render(request, 'modifier_produit.html', {'form': form, 'produit': produit})
