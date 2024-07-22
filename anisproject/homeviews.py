from django.shortcuts import render

from anisproject.models import Produit


def home(request):
        produits = Produit.objects.all()
        return render(request, 'home.html', {'produits': produits})
