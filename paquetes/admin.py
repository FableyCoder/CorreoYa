from django.contrib import admin
from .models import Etiqueta, PaquetePermit

class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PaquetePermitAdmin(admin.ModelAdmin):
    list_display=('title', 'apertura', 'aprobador')
    readonly_fields=('created', 'updated')
    ordering=('title', 'apertura')
    search_fields=('title', 'aprobador__username')
    save_on_top=True

admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(PaquetePermit, PaquetePermitAdmin)