from django.shortcuts import render, HttpResponse, redirect
from productos.models import Producto
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def clientes(request):
    return render(request, 'clientes.html')

def contacto(request):
    return render(request, 'contacto.html')

def empresa(request):
    return render(request, 'empresa.html')

def representacion(request):
    return render(request, 'representacion.html')

def servicios(request):
    return render(request, 'servicios.html')

"""
def crear_producto(request, nombre, descripcion, precio, sku):
    producto = Producto(
        nombre='Primer producto',
        descripcion='Descripcion',
        precio='10000',
        sku='0020'
    )
    producto.save()
    return HttpResponse(f"Producto creado: {producto.nombre}")
"""





def guardar_producto(request):
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        sku = request.POST['sku']
        
        producto = Producto(
            nombre = nombre,
            descripcion = descripcion,
            precio = precio,
            sku = sku
        )
        producto.save()
        
        #Mensaje flash
        messages.success(request, f'Se guardo correctamente el preducto ID {producto.id}')
        return redirect('productos')
    else:
        return HttpResponse("<h2>No se guardo el producto</h2>")

def crear(request):
    return render(request, 'crear_producto.html')
    
    
    
def producto(request):
    try:
        producto = Producto.objects.get(nombre="primer producto")
        response = f"Producto: {producto.id} {producto.nombre}"
    except:
        response = "<h1>Producto no encontrado</h1>"
    return HttpResponse(response)
    
    
def editar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    
    return HttpResponse(f"Producto editado")
        
def productos(request):
    
    productos = Producto.objects.all().order_by('-id')
    
    return render(request, 'productos.html', {
        'productos': productos
    })
    
def borrar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return redirect('productos')
    