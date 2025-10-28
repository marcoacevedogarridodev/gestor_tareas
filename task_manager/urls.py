from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('lista_tareas')),
    path('tareas/', include('tareas.urls')),
]

admin.site.site_header = "Administración de Gestor de Tareas"
admin.site.site_title = "Gestor de Tareas"
admin.site.index_title = "Bienvenido al Panel de Administración"

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Administración de Gestor de Tareas")
admin.site.site_title = _("Gestor de Tareas")
admin.site.index_title = _("Bienvenido al Panel de Administración")