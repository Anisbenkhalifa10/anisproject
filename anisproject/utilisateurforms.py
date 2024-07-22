from django import forms
from .utilisateurmodes import Utilisateur

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom_utilisateur', 'mot_de_passe', 'email', 'role']
        widgets = {
            'mot_de_passe': forms.PasswordInput(),
        }
