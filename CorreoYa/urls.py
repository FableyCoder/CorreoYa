from django.contrib import admin
from django.urls import path
from Core import views as views_core
from opiniones import views as views_opi
from django.conf import settings

urlpatterns = [
    path('', views_core.home, name='home'),
    path('quien/', views_core.quien, name='quien'),
    path('pregunta/', views_core.pregunta, name='pregunta'),
    path('foro/', views_opi.foro, name='foro'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)