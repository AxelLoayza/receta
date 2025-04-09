from django.urls import path
from .views import obtener_recetas, guardar_receta, buscar_recetas_spoonacular

urlpatterns = [
    path('recetas/', obtener_recetas, name='obtener_recetas'),
    path('recetas/nueva/', guardar_receta, name='guardar_receta'),
    path('external-recipes/', buscar_recetas_spoonacular, name='buscar_recetas_spoonacular'),
]