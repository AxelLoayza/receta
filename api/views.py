from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import Receta

API_KEY = "830de5e5888b4914a13fbbd0ed54ab6b"

def obtener_recetas(request):
    recetas = list(Receta.objects.values())  
    return JsonResponse({"recetas": recetas}, safe=False)

@csrf_exempt  
def guardar_receta(request):
    if request.method == "POST":
        datos = json.loads(request.body)
        receta = Receta.objects.create(
            nombre=datos["nombre"],
            ingredientes=",".join(datos["ingredientes"]),
            instrucciones=datos.get("instrucciones", "")
        )
        return JsonResponse({"mensaje": "Receta guardada", "id": receta.id}, status=201)

def buscar_recetas_spoonacular(request):
    ingredientes = request.GET.get("ingredientes", "")
    URL = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": API_KEY,
        "includeIngredients": ingredientes,
        "number": 5
    }
    respuesta = requests.get(URL, params=params)
    return JsonResponse(respuesta.json(), safe=False)