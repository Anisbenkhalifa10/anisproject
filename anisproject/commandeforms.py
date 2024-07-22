from django import forms
from .commandemodels import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['date_commande', 'nom_client', 'montant_total']
