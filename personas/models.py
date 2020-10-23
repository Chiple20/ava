from django.db import models

# Create your models here.
class Alumno(models.Model):
    id_alumno        = models.AutoField(db_column='id_alumno', primary_key=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    rut              = models.CharField(max_length=10, unique=True)
    nombre           = models.CharField(max_length=20, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=20, blank=True, null=True)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    genero           = models.CharField(max_length=10, blank=True, null=True)
    foto             = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo           = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.rut+", " + self.nombre+", " + self.apellido_paterno+ ", "+self.apellido_materno + ", " +self.foto.__str__()

    class Meta:
        ordering=["rut"]
