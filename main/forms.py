from django import forms

class BuscarRecetaForm(forms.Form):
    ingredientes = forms.CharField(label="Ingredientes (separados por comas)", max_length=200)
    