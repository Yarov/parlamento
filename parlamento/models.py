from django.db import models

class TimestampedModel(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    class Meta:
        abstract = True


class Entidad(TimestampedModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Partido(TimestampedModel):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/partidos')
    tipot = models.IntegerField()
    
    def __str__(self):
        return self.name


class Diputado(TimestampedModel):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/diputados')
    type_lection = models.CharField(max_length=50)
    distrit = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    suplente = models.CharField(max_length=100)
    entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT)
    partido = models.ForeignKey(Partido, on_delete=models.PROTECT)
