from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
from django.utils import timezone
class Portafolio(models.Model):
    proyecto    = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_crea  = models.DateTimeField(auto_now_add=True)
    fecha_publ  = models.DateTimeField(auto_now=True, null=True)
    
    def publish(self):
        self.fecha_publ = timezone.now()
        self.save()
    
    def __str__(self):
        return self.proyecto
    
    class Meta:
        permissions = (
            ('profesor',_('Es profesor')),
            ('alumno',_('Es alumno')),
        )