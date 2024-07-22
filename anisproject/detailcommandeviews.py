from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .detailcommandemodels import DetailCommande
from .commandemodels import Commande
from .models import Produit
from .detailcommandeforms  import DetailCommandeForm
@login_required
def liste_detail_commandes(request):
    details = DetailCommande.objects.all()
    return render(request, 'detailcommandes/liste_detail_commandes.html', {'details': details})

@login_required
def ajouter_detail_commande(request):
    if request.method == 'POST':
        form = DetailCommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_detail_commandes')
    else:
        form = DetailCommandeForm()

    commandes = Commande.objects.all()
    produits = Produit.objects.all()

    return render(request, 'detailcommandes/ajouter_detail_commande.html', {
        'form': form,
        'commandes': commandes,
        'produits': produits
    })
@login_required
def modifier_detail_commande(request, detail_id):
    detail = get_object_or_404(DetailCommande, id=detail_id)

    if request.method == 'POST':
        form = DetailCommandeForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('liste_detail_commandes')
    else:
        form = DetailCommandeForm(instance=detail)
        commandes = Commande.objects.all()
        produits = Produit.objects.all()

    return render(request, 'detailcommandes/modifier_detail_commande.html', {
        'form': form,
        'commandes': commandes,
        'produits': produits,

    })
@login_required
def supprimer_detail_commande(request, detail_id):
    detail = get_object_or_404(DetailCommande, id=detail_id)
    if request.method == 'POST':
        detail.delete()
        return redirect('liste_detail_commandes')
    return render(request, 'detailcommandes/supprimer_detail_commande.html', {'detail': detail})
