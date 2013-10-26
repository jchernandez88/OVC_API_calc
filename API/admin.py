from django.contrib import admin
from models import Operacion

class OperacionAdmin(admin.ModelAdmin):
    list_display = ('op1','operacion','op2','resultado')
        
admin.site.register(Operacion,OperacionAdmin)