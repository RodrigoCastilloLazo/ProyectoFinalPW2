from django.db import models
from django.contrib.auth.models import User
from estudiantes.models import Alumno
from cursos.models import Asignatura, CursoTeo

class CambioGrupo(models.Model):
    cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    cui_solicitante = models.ForeignKey(Alumno, related_name='solicitante', on_delete=models.CASCADE)
    cui_donante = models.ForeignKey(Alumno, related_name='donante', on_delete=models.CASCADE)
    num = models.IntegerField()
    curso_solicitante = models.ForeignKey(CursoTeo, related_name='curso_solicitante', on_delete=models.CASCADE)
    curso_donante = models.ForeignKey(CursoTeo, related_name='curso_donante', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    class Meta:
        unique_together = ('cod_asignatura', 'cui_solicitante', 'cui_donante', 'num')

    def __str__(self):
        return f"{self.cod_asignatura} - {self.cui_solicitante} - {self.cui_donante}"
