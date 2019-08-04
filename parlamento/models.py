from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify

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
    slug = models.CharField(max_length=250)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Diputado,self).save(*args, **kwargs)


class Iniciativa(TimestampedModel):
    TYPE_REPRESENTATION_CHOICES = [
        ('GROUP', 'De grupo'),
        ('ADHERENT', 'Adherente'),
        ('INITIATOR', 'Iniciante'),
        ('DIVGROUP', 'Diversos grupos parlamentarios'),
    ]

    STATUS_CHOISES = [
        ('APPROVED', 'Aprobada'),
        ('ATTENDED', 'Atendidas'),
        ('REJECTED', 'Desechadas'),
        ('DECLINED', 'Retiradas'),
        ('PENDING', 'Pendientes'),
    ]
    description = models.TextField()
    sinopsis = models.TextField()
    type_presentation = models.CharField(
        max_length=50,
        choices=TYPE_REPRESENTATION_CHOICES
    )
    status = models.CharField(
        max_length =20,
        choices=STATUS_CHOISES
    )
    date_presentation = models.DateTimeField()
    date_status = models.DateTimeField()
    diputado = models.ForeignKey(Diputado, on_delete=models.PROTECT)
    def __str__(self):
        return self.description
    
