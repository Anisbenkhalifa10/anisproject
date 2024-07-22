from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .commandemodels import Commande
from .commandeforms import CommandeForm
@login_required
def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'commande/liste_commandes.html', {'commandes': commandes})
@login_required
def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_commandes')
    else:
        form = CommandeForm()
    return render(request, 'commande/ajouter_commande.html', {'form': form})
@login_required
def modifier_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('liste_commandes')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'commande/modifier_commande.html', {'form': form, 'commande': commande})
@login_required
def supprimer_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    if request.method == 'POST':
        commande.delete()
        return redirect('liste_commandes')
    return render(request, 'commande/supprimer_commande.html', {'commande': commande})
