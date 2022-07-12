from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import AnimalFormulario,PersonaFormulario,UserRegisterForm
from AppCoder.models import Animal,Persona,Veterinario
#CVB
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#-Loguin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.



def inicio(request):
    return render(request,"AppCoder/inicio.html")



#-----------------------------------------Mascota-------------------------------------------------------
def animal(request):
    return render(request,"AppCoder/animal.html")

def leerMascota(request):
    mascotas = Animal.objects.all()
    contexto = {"mascotas":mascotas}
    return render(request,"AppCoder/animal.html",contexto)

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


#-----------------------------------------Persona-------------------------------------------------------
def persona(request):
    return render(request,"AppCoder/persona.html")

def leerPersona(request):
    personas = Persona.objects.all()
    contexto = {"personas":personas}
    return render(request,"AppCoder/persona.html",contexto)

def formularioPersona(request):

    if request.method == 'POST':
        miFormularioPersona = PersonaFormulario(request.POST)
        print(miFormularioPersona)

        if miFormularioPersona.is_valid:
            
            informacion = miFormularioPersona.cleaned_data
		    
            persona = Persona(nombre=informacion['nombre'],
            apellido=informacion['apellido'],telefono=informacion['telefono'])
		    
            persona.save()

            personas = Persona.objects.all()
            
            return render(request,"AppCoder/persona.html",{"personas":personas})

    else:
        miFormularioPersona = PersonaFormulario()
    return render(request, "AppCoder/formularioPersona.html",{"miFormularioPersona":miFormularioPersona})


def editarPersona(request,persona_nombre):

    persona = Persona.objects.get(nombre = persona_nombre)

    if request.method == 'POST':
        miFormularioPersona = PersonaFormulario(request.POST)
        print(miFormularioPersona)

        if miFormularioPersona.is_valid:
            
            informacion = miFormularioPersona.cleaned_data
		    
            persona.nombre=informacion['nombre']
            persona.apellido=informacion['apellido']
            persona.telefono=informacion['telefono']
		    
            persona.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioPersona= PersonaFormulario(initial={'nombre': persona.nombre, 'apellido':persona.apellido , 
            'telefono':persona.telefono}) 
    
    return render(request, "AppCoder/editarPersona.html", {"miFormularioPersona": miFormularioPersona, "persona_nombre":persona_nombre})
        

def eliminarPersona(request,persona_nombre):
    persona = Persona.objects.get(nombre=persona_nombre)
    persona.delete()
    personas = Persona.objects.all()
    contexto ={"personas":personas}
    return render(request,"AppCoder/persona.html",contexto)

#-----------------------------------------PersonaCBV-------------------------------------------------------

class PersonaList(ListView):
    model= Persona
    template_name= "AppCoder/persona_list.html"



class PersonaDetalle(DetailView): 
    model=Persona
    template_name= "AppCoder/persona_detalle.html"



class PersonaCreacion(CreateView):
    model= Persona
    succcess_url = "/AppCoder/persona/list"	
    fields = ['nombre','apellido','telefono']




class PersonaUpdate(UpdateView):
    
    model= Persona
    succcess_url = "/AppCoder/persona/list"	
    fields = ['nombre','apellido','telefono']




class CursoDelete(DeleteView):  
    model= Persona
    succcess_url = "/AppCoder/persona/list"	



#-----------------------------------------Veterinario-------------------------------------------------------
def veterinario(request):
    return render(request,"AppCoder/veterinario.html")



#-----------------------------------------Loguin/Register-------------------------------------------------------
def login_request(request):
    if request.method == 'POST':

        form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario,password = contra)

            if user is not None:
                login(request,user)
                return render(request,"AppCoder/inicio.html",{"mensaje":f"Bienvenido{usuario}"})
            else:
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error,datos incorrectos"})

        else:
            return render(request,"AppCoder/inicio.html",{"mensaje":"Error,formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppCoder/login.html",{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html",{"mensaje":"Usuario Creado :)"})
    else:
        #form = UserRegisterForm()
        form = UserCreationForm()
    return render(request,"AppCoder/registro.html",{"form":form})

@login_required
def inicio(request):
    return render(request,"AppCoder/inicio.html")