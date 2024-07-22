from django import forms
from .detailcommandemodels import DetailCommande


class DetailCommandeForm(forms.ModelForm):
    class Meta:
        model = DetailCommande
        fields = ['id_commande', 'id_produit', 'quantite', 'prix_unitaire']
        widgets = {
            'id_commande': forms.Select(attrs={'class': 'form-control'}),
            'id_produit': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control'}),
        }
