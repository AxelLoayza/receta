from django.shortcuts import render
import requests
from .models import Receta
from .forms import BuscarRecetaForm

API_KEY = "TU_API_KEY"

def buscar_recetas(request):
    recetas_locales = None
    recetas_externas = None
    
    if request.method == "POST":
        form = BuscarRecetaForm(request.POST)
        if form.is_valid():
            ingredientes = form.cleaned_data['ingredientes'].split(",")

            
            URL = "https://api.spoonacular.com/recipes/complexSearch"
            params = {
                "apiKey": API_KEY,
                "includeIngredients": ",".join(ingredientes),
                "number": 5
            }
            respuesta = requests.get(URL, params=params)
            recetas_externas = respuesta.json().get("results", [])

         
            recetas_locales = Receta.objects.filter(ingredientes__icontains=ingredientes[0])
    else:
        form = BuscarRecetaForm()

    return render(request, "recetas/buscar.html", {
        "form": form,
        "recetas_locales": recetas_locales,
        "recetas_externas": recetas_externas,
    })