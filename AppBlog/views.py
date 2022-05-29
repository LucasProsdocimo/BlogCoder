from django.shortcuts import render
from AppBlog.forms import FormularioPosteo, FormularioComentario, FormularioBusqueda, FormularioUsuario
from AppBlog.models import Usuario, Posteo, Comentario

def inicio(request):

    id = 1
    listadoPosteos = Posteo.objects.all()
    diccionario = {'id': id, 'listadoPosteos': listadoPosteos}
    return render(request,'AppBlog/inicio.html', diccionario)

def sobreNostros(request):

    id = 2
    diccionario = {'id': id}
    return render(request,'AppBlog/sobreNosotros.html', diccionario)

def hacerPosteo(request):

    if request.method == 'POST':

        miPosteo = FormularioPosteo(request.POST)

        print(miPosteo)

        if miPosteo.is_valid():

            contenido = miPosteo.cleaned_data

            posteo = Posteo(autor = contenido['autor'], email = contenido['email'], titulo = contenido['titulo'], cuerpo = contenido['cuerpo'])

            posteo.save()

            return render(request,'AppBlog/inicio.html')
    else:

        miPosteo = FormularioPosteo()

    id = 3
    diccionario = {'id': id, 'miPosteo': miPosteo}
    return render(request,'AppBlog/hacerPosteo.html', diccionario)

def buscar(request):

    data = request.GET.get('titulo', '')

    error = ''

    if data:

        try:
            posteo = Posteo.objects.get(titulo = data)
            return render(request, 'AppBlog/buscar.html', {'posteo': posteo, 'titulo': data})

        except Exception as exc:
            print(exc)
            error = '¡No se encontraron posteos con el título indicado!'

    id = 4
    diccionario = {'id': id, 'error': error}
    return render(request,'AppBlog/buscar.html', diccionario)

def abrirPosteo(request, titulo):

        leerPosteo = Posteo.objects.get(titulo = titulo)

        try:
            comentario = Comentario.objects.get(titulo = titulo)

            return render(request, 'appBlog/posteo.html', {'posteo': leerPosteo, 'comentario': comentario})
        
        except:

            return render(request, 'appBlog/posteo.html', {'posteo': leerPosteo})