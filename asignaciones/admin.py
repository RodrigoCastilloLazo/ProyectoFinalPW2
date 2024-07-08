from django.contrib import admin
from .models import AsignacionLab, AsignacionTeo 
class AsignacionLabAdmin(admin.ModelAdmin):
    list_display = ('cui', 'cod_curso', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cui__cui', 'cod_curso__cod_curso')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        else:
            obj.user_id = request.user
        obj.save()

admin.site.register(AsignacionLab, AsignacionLabAdmin)

class AsignacionTeoAdmin(admin.ModelAdmin):
    list_display = ('cui', 'cod_curso', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cui__cui', 'cod_curso__cod_curso')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        else:
            obj.user_id = request.user
        obj.save()

admin.site.register(AsignacionTeo, AsignacionTeoAdmin)