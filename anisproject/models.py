from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    image = models.ImageField(upload_to="produits/", null=True, blank=True)


    class Meta:
        db_table = 'Produit'

