from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import AnimalFormulario
from AppCoder.models import Animal 
# Create your views here.



def inicio(request):
    return render(request,"AppCoder/inicio.html")

def animal(request):
    return render(request,"AppCoder/animal.html")

def persona(request):
    return render(request,"AppCoder/persona.html")

def veterinario(request):
    return render(request,"AppCoder/veterinario.html")


def formularioMascota(request):

    if request.method == 'POST':
        miFormulario = AnimalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            mascota = Animal(nombreAnimal=informacion['nombreAnimal'],
            edad=informacion['edad'],tipo=informacion['tipo'],
            motivo=informacion['motivo'],fecha=informacion['fecha'],
            costo=informacion['costo'])
		    
            mascota.save()

            mascotas = Animal.objects.all()
    

            return render(request,"AppCoder/animal.html",{"mascotas":mascotas})

    else:
        miFormulario = AnimalFormulario()
    return render(request, "AppCoder/formularioMascota.html",{"miFormulario":miFormulario})

#------------------------------------------------------------------------------------------------
def busquedaMascota(request):
    return render(request,"AppCoder/busquedaMascota.html")

def buscar(request):
        
    if request.GET["nombreAnimal"]:
        nombreAnimal = request.GET['nombreAnimal']
        mascotas = Animal.objects.filter(nombreAnimal__icontains=nombreAnimal)
        
        return render(request, "AppCoder/animal.html",{"mascotas":mascotas})

    else:
        respuesta = "No enviaste nada"
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})

# respuesta=f"Estoy buscando el nombre de: {request.GET['nombreAnimal']}"

        # return HttpResponse(respuesta)
        