from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField() 
    instrucciones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre