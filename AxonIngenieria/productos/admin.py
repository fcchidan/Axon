from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)

# configurar el titulo del panel de administracion
title = "Axon Ingeniería Eléctrica"
admin.site.site_header = title
admin.site.site_title = title