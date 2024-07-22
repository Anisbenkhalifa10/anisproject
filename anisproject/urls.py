from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views, fournisseurviews, utilisateurviews, commandeviews, detailcommandeviews, homeviews, loginviews, \
    logoutviews
from .rechercheviwes import search_view

urlpatterns = [
path('', homeviews.home, name='home'),
    path('search/', search_view, name='search'),
    path('admin/login/', loginviews.admin_login, name='admin_login'),
    path('logout/', logoutviews.logout_view, name='logout'),
    path('produit/', views.liste_produits, name='liste_produits'),
    path('produit/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    # Ajoute d'autres URL patterns pour tes vues ici
    path('produit/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
path('modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('fournisseurs/', fournisseurviews.liste_fournisseurs, name='liste_fournisseurs'),
# Dans urls.py de l'application 'fournisseur'
    path('fournisseurs/', fournisseurviews.liste_fournisseurs, name='liste_fournisseurs'),
    path('fournisseurs/ajouter/', fournisseurviews.ajouter_fournisseur, name='ajouter_fournisseur'),
path('fournisseurs/supprimer/<int:fournisseur_id>/', fournisseurviews.supprimer_fournisseur, name='supprimer_fournisseur'),

    path('fournisseurs/<int:fournisseur_id>/modifier/', fournisseurviews.modifier_fournisseur, name='modifier_fournisseur'),
    path('utilisateurs/', utilisateurviews.liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateurs/ajouter/', utilisateurviews.ajouter_utilisateur, name='ajouter_utilisateur'),
    path('utilisateurs/<int:utilisateur_id>/modifier/', utilisateurviews.modifier_utilisateur, name='modifier_utilisateur'),
    path('utilisateurs/<int:utilisateur_id>/supprimer/', utilisateurviews.supprimer_utilisateur, name='supprimer_utilisateur'),
path('commandes/', commandeviews.liste_commandes, name='liste_commandes'),
    path('commandes/ajouter/', commandeviews.ajouter_commande, name='ajouter_commande'),
    path('commandes/supprimer/<int:commande_id>/', commandeviews.supprimer_commande, name='supprimer_commande'),
    path('commandes/modifier/<int:commande_id>/', commandeviews.modifier_commande, name='modifier_commande'),
 path('detailcommandes/', detailcommandeviews.liste_detail_commandes, name='liste_detail_commandes'),
    path('detailcommandes/ajouter/', detailcommandeviews.ajouter_detail_commande, name='ajouter_detail_commande'),
    path('detailcommandes/<int:detail_id>/modifier/', detailcommandeviews.modifier_detail_commande, name='modifier_detail_commande'),
    path('detailcommandes/<int:detail_id>/supprimer/', detailcommandeviews.supprimer_detail_commande, name='supprimer_detail_commande'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



