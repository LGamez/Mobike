from django import forms

class PortafolioForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.CharField(label="E-Mail", required=True)
    content = forms.CharField(label="Contenido", required=True)