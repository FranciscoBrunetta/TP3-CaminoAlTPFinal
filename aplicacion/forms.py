from django import forms

class VinoForm(forms.Form):
    categoria = forms.CharField(label="Categoria del Vino", max_length=50, required=True)
    varietal = forms.CharField(label="Varietal", max_length=50, required=True)