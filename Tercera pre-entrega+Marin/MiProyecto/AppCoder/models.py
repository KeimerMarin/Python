from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'AppCoder'  

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        app_label = 'AppCoder' 

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        app_label = 'AppCoder' 
