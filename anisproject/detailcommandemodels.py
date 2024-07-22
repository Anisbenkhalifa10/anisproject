from django.db import models

from anisproject.commandemodels import Commande
from anisproject.models import Produit


class DetailCommande(models.Model):
    id = models.AutoField(primary_key=True)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE, db_column='id_commande')
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE, db_column='id_produit')
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'DetailCommande'
