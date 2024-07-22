from django.shortcuts import render
from .models import Produit

def search_view(request):
    query = request.GET.get('q')
    results = Produit.objects.filter(nom__icontains=query) if query else []
    context = {
        'produits': results,
        'query': query
    }
    return render(request, 'home.html', context)
