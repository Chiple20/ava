from django.shortcuts import render
from .models import Alumno


   

# Create your views here.
def index(request):
    print("ok,estamos en la vista")
    context={   }
    return render(request, 'personas/index.html', context)

def listar(request):
    print("ok,estamos en la vista listar")
    context={   }
    return render(request, 'personas/listar.html', context)

def mostrar_alumnos(request):
    print("ok,estamos en la vista mostrar_alumnos")
    lista= Alumno.objects.all()
    context={ 'listado':lista  }
    return render(request, 'personas/listar_alumnos.html', context)

def buscar(request):
    print("ok,estamos en la vista buscar")
    context={   }
    return render(request, 'personas/buscar.html', context)



def eliminar(request):
    print("ok,estamos en la vista eliminar")
    context={   }
    return render(request, 'personas/eliminar.html', context)

def eliminar_por_rut(request):
    print("hola  estoy en eliminar_por_rut_por_rut...")
    if request.method == 'POST':
       mi_rut = request.POST['rut']

       if mi_rut != "":
           try:
               alumno = Alumno()
               alumno= Alumno.objects.get(rut=mi_rut)
               if alumno is not None:
                   print("Alumno=", alumno)
                   alumno.delete()
                   return render(request, 'personas/mensaje_alumno_eliminado.html', )
               else:
                   return render(request, 'personas/error/error_202.html',{})
           except alumno.DoesNotExist:
               return render(request, 'personas/error/error_202.html', {})
       else:
           return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def agregar(request):
    print("ok,estamos en la vista agregar")
    
    context={   }
    return render(request, 'personas/formulario_agregar.html', context)

def agregar_alumno(request):
    print("hola  estoy en agregar_alumno...")
    if request.method == 'POST':
       mi_rut = request.POST['rut']
       mi_nombre= request.POST['nombre']
       mi_paterno=request.POST['aPaterno']
       mi_materno=request.POST['aMaterno']
       mi_fechaNac =request.POST['fechaNac']
       mi_genero=request.POST['genero']
       mi_foto = request.FILES['foto']

 

       if mi_rut != "":
           try:
               alumno = Alumno()

               alumno.rut = mi_rut
               alumno.nombre = mi_nombre
               alumno.apellido_paterno = mi_paterno
               alumno.apellido_materno = mi_materno
               alumno.fecha_nacimiento = mi_fechaNac
               alumno.genero = mi_genero
               alumno.foto = mi_foto

               alumno.save()

               return render(request, 'personas/mensaje_datos_guardados.html',{})

           except alumno.DoesNotExist:
               return render(request, 'personas/error/error_204.html', {})
       else:
           return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})

def buscar_por_rut(request):
    print("hola  estoy en buscar_por_rut...")
    if request.method == 'POST':
       mi_rut = request.POST['rut']

       if mi_rut != "":
           try:
               alumno = Alumno()
               alumno= Alumno.objects.get(rut=mi_rut)
               if alumno is not None:
                   print("Alumno=", alumno)
                   context={'alumno':alumno}
                   return render(request, 'personas/mostrar_datos.html', context)
               else:
                   return render(request, 'personas/mensaje_alumno_elminado.html',{})
           except alumno.DoesNotExist:
               return render(request, 'personas/error/mensaje_alumno_elminado.html', {})
       else:
           return render(request, 'personas/error/mensaje_alumno_elminado.html', {})
    else:
        return render(request, 'personas/error/mensaje_alumno_elminado.html', {})
def editar(request):
    print("ok,estamos en la vista editar")
    context={   }
    return render(request, 'personas/boton_editar.html', context)

def buscar_para_editar(request):

    print("hola  estoy en buscar_para_editar...")
    if request.method == 'POST':
        mi_rut = request.POST['rut']

        if mi_rut != "":
            try:
                alumno = Alumno()
                alumno = Alumno.objects.get(rut=mi_rut)
                if alumno is not None:
                    print("Alumno=", alumno)
                    context = {'alumno': alumno}
                    return render(request, 'personas/formulario_editar.html', context)
                else:
                    return render(request, 'personas/error/error_202.html', {})
            except alumno.DoesNotExist:
                return render(request, 'personas/error/error_202.html', {})
        else:
            return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def actualizar_alumno(request):
    print("hola  estoy en actualizar_alumno...")
    if request.method == 'POST':
       mi_id  = request.POST['id_alumno']
       mi_rut = request.POST['rut']
       mi_nombre= request.POST['nombre']
       mi_paterno=request.POST['aPaterno']
       mi_materno=request.POST['aMaterno']
       mi_fechaNac =request.POST['fechaNac']
       mi_genero=request.POST['genero']
       mi_foto = request.FILES['foto']

       if mi_rut != "":
           try:
               alumno = Alumno()

               alumno.id_alumno = mi_id
               alumno.rut = mi_rut
               alumno.nombre = mi_nombre
               alumno.apellido_paterno = mi_paterno
               alumno.apellido_materno = mi_materno
               alumno.fecha_nacimiento = mi_fechaNac
               alumno.genero = mi_genero
               alumno.activo = 1
               alumno.foto = mi_foto

               alumno.save()  #actualiza

               return render(request, 'personas/mensaje_datos_guardados.html',{})

           except alumno.DoesNotExist:
               return render(request, 'personas/error/error_204.html', {})
       else:
           return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def menu(request):
    print("ok,estamos en la vista menu")
    alumnos= Alumno.objects.all()
    context={ 'alumnos':alumnos  }
    return render(request, 'personas/menu_alumno.html', context)
def menu_productos(request):
    print("ok,estamos en la vista menu")
    alumnos= Alumno.objects.all()
    context={ 'alumnos':alumnos  }
    return render(request, 'personas/menu_productos.html', context)
