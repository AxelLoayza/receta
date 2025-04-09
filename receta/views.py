import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import BuscarRecetaForm
from api.models import Receta  


API_URL_BUSCAR = "http://127.0.0.1:8000/api/external-recipes"
API_URL_GUARDAR = "http://127.0.0.1:8000/api/recetas/nueva/"

def buscar_recetas(request):
    """ Vista para buscar recetas en la base de datos y Spoonacular """
    recetas_externas = []
    recetas_locales = []

    if request.method == "POST":
        form = BuscarRecetaForm(request.POST)
        if form.is_valid():
            ingredientes = form.cleaned_data["ingredientes"]

          
            response = requests.get(API_URL_BUSCAR, params={"ingredientes": ingredientes})
            if response.status_code == 200:
                recetas_externas = response.json().get("results", [])

            recetas_locales = Receta.objects.filter(ingredientes__icontains=ingredientes)
    else:
        form = BuscarRecetaForm()

    return render(request, "receta/buscar.html", {
        "form": form,
        "recetas_locales": recetas_locales,
        "recetas_externas": recetas_externas
    })

@csrf_exempt 
def guardar_receta(request):
    """ Vista para guardar una receta en la base de datos """
    if request.method == "POST":
        datos = {
            "nombre": request.POST["nombre"],
            "ingredientes": request.POST["ingredientes"].split(",")
        }

        
        response = requests.post(API_URL_GUARDAR, json=datos)
        if response.status_code == 201:
            return redirect("buscar_recetas")
    
    return redirect("buscar_recetas")