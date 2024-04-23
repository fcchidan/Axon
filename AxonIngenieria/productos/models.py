

# Tu código sigue aquí...


from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(default='null', upload_to="productos")
    descripcion = models.TextField()
    precio = models.IntegerField()
    sku = models.IntegerField()
    
    def __str__(self):
        return f"Nombre producto: {self.nombre} precio: {self.precio} SKU: {self.sku}"
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
