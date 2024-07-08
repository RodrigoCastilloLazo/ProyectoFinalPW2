from django.contrib import admin
from .models import CambioGrupo

class CambioGrupoAdmin(admin.ModelAdmin):
    list_display = ('cod_asignatura', 'cui_solicitante', 'cui_donante', 'num', 'curso_solicitante', 'curso_donante', 'status', 'created', 'modified', 'user_id')
    search_fields = ('cod_asignatura__cod_asignatura', 'cui_solicitante__cui', 'cui_donante__cui')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.user = request.user
        obj.save()

admin.site.register(CambioGrupo,CambioGrupoAdmin)