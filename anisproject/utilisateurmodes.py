from django.db import models

class Utilisateur(models.Model):
    nom_utilisateur = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, null=True, blank=True)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('utilisateur', 'Utilisateur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        db_table = 'Utilisateur'
