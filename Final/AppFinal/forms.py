from django import forms

class ReservaFormulario(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Apellido = forms.CharField(max_length=50)
    Correo = forms.CharField(max_length=50)
    Cantidad_Boletos= forms.IntegerField()

class ContactoFormulario(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Correo = forms.CharField(max_length=50)
    Mensaje= forms.CharField(max_length=200)


class TrabajaFormulario(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Apellido = forms.CharField(max_length=50)
    Correo = forms.EmailField()
    URL_Linkedin= forms.URLField()