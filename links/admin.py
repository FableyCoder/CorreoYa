from django.contrib import admin
from .models import RedSocial

class RedSocialAdmin(admin.ModelAdmin):
    pass
admin.site.register(RedSocial, RedSocialAdmin)
