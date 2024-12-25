from django.db import models

# Create your models here.

class Kategoria(models.Model):
    nazwa_kategorii = models.CharField(max_length=50)
    opis = models.TextField(max_length=200)

    def __str__(self):
        return self.nazwa_kategorii

class Alergeny(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa_alergenu = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa_alergenu

class Menu(models.Model):
    nazwa_dania = models.CharField(max_length=50)
    opis = models.TextField(max_length=200)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    alergeny = models.ManyToManyField(Alergeny, related_name='dania')

    def __str__(self):
        return f'{self.nazwa_dania} {self.kategoria} {self.cena}'    
    
class Promocje(models.Model):
    nazwa_promocji = models.CharField(max_length=50)
    opis = models.TextField(max_length=200)
    obraz = models.ImageField(upload_to='promocje', null=True, blank=True)

    def __str__(self):
        return self.nazwa_promocji