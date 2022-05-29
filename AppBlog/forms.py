from django import forms

class FormularioUsuario(forms.Form):
    
    nombre = forms.CharField(max_length = 40)
    apellido = forms.CharField(max_length = 40)
    dni = forms.IntegerField()

class FormularioPosteo(forms.Form):

    autor = forms.CharField(max_length = 40)
    email = forms.EmailField()
    titulo = forms.CharField(max_length = 40)
    cuerpo = forms.CharField(widget=forms.Textarea)

class FormularioComentario(forms.Form):

    autor = forms.CharField(max_length = 40)
    email = forms.EmailField()
    cuerpo = forms.CharField(widget=forms.Textarea)

class FormularioBusqueda(forms.Form):

    titulo = forms.CharField(max_length=40)