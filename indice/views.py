# from django.template import Context
# from django.template import Template
from django.template import loader
from django.http import HttpResponse
import random

def inicio(request):
    return HttpResponse ('Hola, soy la nueva pagina')

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo</h1>
                        ''')
    
def numero_random(request):
    numero = random.randrange(15, 180)
    texto = f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    # plantilla = open(r"C:\Users\Martin H. Taraciuk\Desktop\miproyecto\miproyecto\plantillas\mi_plantilla.html")
    # template = Template(plantilla.read())
    # context = Context(diccionario_de_datos)
    # plantilla.close()
    
    
    nombre = 'jorge'
    apellido = 'Atahualpa'
    
    lista = [3,1,2,34,1,2,3]
    
    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista
    }
    
    template = loader.get_template("mi_plantilla.html")
    
    plantilla_preparada = template.render(diccionario_de_datos)
    
    return HttpResponse(plantilla_preparada)