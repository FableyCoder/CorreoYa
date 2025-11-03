from django.contrib import admin
from django.urls import path, include
from Core import views as views_core
from opiniones import views as views_opi
from paquetes import views as views_paq
from django.conf import settings

urlpatterns = [
    path('', views_core.home, name='home'),
    path('quien/', views_core.quien, name='quien'),
    path('paquete/', views_paq.paquetes, name='EjemplosPaquetes'),
    path('etiquetas/<int:etiqueta_id>', views_paq.etiqueta, name="Etiquetas"),
    path('foro/', views_opi.opinion, name='foro'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)