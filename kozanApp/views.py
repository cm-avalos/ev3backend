from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from kozanApp.forms import FormEmpleado,FormEquipo, FormArea
from kozanApp.models import Empleado,Equipos,Area
from . import forms

def index(request):
    return render(request, 'kozanApp/index.html')

def listadoEmpleados(request):
    empleados = Empleado.objects.all()
    data = {'empleados': empleados}
    return render(request, 'kozanApp/empleados.html', data)

def agregarEmpleados(request):
    form = FormEmpleado()
    if request.method == 'POST':
        form = FormEmpleado(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/agregarEmpleados.html', data)

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    empleado.delete()
    return redirect('/empleados',)

def actualizarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    form = FormEmpleado(instance=empleado)
    if request.method == 'POST':
        form = FormEmpleado(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/agregarEmpleados.html', data)

    ############################################################################################################################

    #equipo

    #############################################################################################################################



def listadoEquipos(request):
    equipos = Equipos.objects.all()
    data = {"equipos":equipos}
    return render(request,'kozanApp/equipos.html',data)

def agregarEquipo(request):
    form = FormEquipo()
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'kozanApp/registrarEquipo.html',data)


def eliminarEquipo(request,id):
    equipos=Equipos.objects.get(id=id)
    equipos.delete()
    return redirect('/equipos')


def actualizarEquipo(request,id):
    equipo = Equipos.objects.get(id=id)
    form = FormEquipo(instance=equipo)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'kozanApp/registrarEquipo.html',data)

    ############################################################################################################################

    #areas

    #############################################################################################################################


def listadoAreas(request):
    areas = Area.objects.all()
    data = {'areas': areas}
    return render(request, 'kozanApp/areas.html', data)

def agregarAreas(request):
    form = FormArea()
    if request.method == 'POST':
        form = FormArea(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/registrarArea.html', data)

def eliminarAreas(request, id):
    area = Area.objects.get(id = id)
    area.delete()
    return redirect('/areas',)

def actualizarAreas(request, id):
    area = Area.objects.get(id = id)
    form = FormArea(instance=area)
    if request.method == 'POST':
        form = FormArea(request.POST, instance=area)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/registrarArea.html', data)