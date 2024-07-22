from django.db import models

class Commande(models.Model):
    date_commande = models.DateField()
    nom_client = models.CharField(max_length=100, null=True, blank=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Commande'
    def __str__(self):
        return f"Commande #{self.id} - {self.nom_client}"
