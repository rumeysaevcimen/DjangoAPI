from django.contrib import admin
from AsgariUcret.models import AsgariUcret


@admin.register(AsgariUcret)
class AsgariUcretAdmin(admin.ModelAdmin):
    pass
