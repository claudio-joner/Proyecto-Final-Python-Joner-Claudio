from django import forms 

class AnimalFormulario(forms.Form):
    nombreAnimal= forms.CharField(max_length=40)
    edad= forms.IntegerField()
    tipo= forms.CharField(max_length=40)
    motivo= forms.CharField(max_length=40)
    fecha= forms.DateField()
    costo= forms.IntegerField()
