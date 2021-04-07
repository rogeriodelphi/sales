from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Tipo'
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    names = models.CharField(max_length=150, verbose_name='Nomes')
    rg = models.CharField(max_length=10, unique=True, verbose_name='RG')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    date_joined = models.DateField(default=datetime.now, verbose_name='Data do Registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    # gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        db_table = 'Empregado'
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'
        ordering = ['-id']