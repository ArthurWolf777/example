"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
import contactos.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contactos.views.index, name="index"),
    path('inicio/', contactos.views.index, name="index"),
    path('contacto/nuevo/', contactos.views.new_contact, name="new_contact"),
    path('contacto/editar/<int:id>/', contactos.views.edit_contact, name="edit_contact"),
    path('contacto/editar/nombre/<int:id>/', contactos.views.edit_name, name="edit_contact_name"),
    path('contacto/editar/direccion/<int:id>/', contactos.views.edit_adress, name="contact_name_ban"),
    path('delete/<int:id>/', contactos.views.delete_contact, name="delete"),
    path('test/', contactos.views.test_code, name="test")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)