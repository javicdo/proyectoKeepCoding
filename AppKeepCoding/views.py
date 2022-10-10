from django.http import HttpResponse
from django.shortcuts import render
from AppKeepCoding.models import Curso

# Create your views here.

def curso(self):
    curso = Curso(nombre="Java",camada=19882)
    curso2 = Curso(nombre="Desarrollo Web",camada=17645)
    curso.save()
    curso2.save()
    texto1 = f"Curso: {curso.nombre}, Camada: {curso.camada}"
    texto2 = f"Curso: {curso2.nombre}, Camada: {curso2.camada}"
    return HttpResponse(texto2)
