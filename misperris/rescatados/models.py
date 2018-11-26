from django.db import models
from datetime import datetime

# Create your models here.

class Estado(models.Model):
    desc_estado = models.CharField(max_length=20)

    def __str__(self):
        return self.desc_estado


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nom_mascota = models.CharField(max_length=20)
    tamano_mascota = models.IntegerField(default=0)
    peso_mascota = models.FloatField(default=0)
    color_mascota = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    fecha_rescate = models.DateField('Fecha Rescate')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Regione(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nom_region = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_region


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=50)
    reg_com = models.ForeignKey(Regione, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_comuna


class Vivienda(models.Model):
    tipo_vivienda = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.tipo_vivienda




class Adoptante(models.Model):
    rut = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=70)
    nombre_full = models.CharField(max_length=100)
    fec_nac = models.DateField(help_text='Fecha de Nacimiento')
    fono = models.PositiveIntegerField(help_text='numero de Telefono')
    comuna = models.CharField(max_length=80)
    region = models.CharField(max_length=80)
    tipo_vivienda = models.CharField(max_length=80)




#utilizamos una fomra distinta de mostrar los resultados a través de una lista en el admin.
