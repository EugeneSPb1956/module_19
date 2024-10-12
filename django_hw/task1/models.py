from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя покупателя')
    balance = models.DecimalField(max_digits=11, null=True, decimal_places=2, verbose_name='Баланс')
    age = models.IntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = 'Книга'
    #     verbose_name_plural = 'Книги'

class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название игры')
    cost = models.DecimalField(max_digits=11, null=True, decimal_places=2, verbose_name='Цена')
    size = models.DecimalField(max_digits=15, null=True, decimal_places=3, verbose_name='Размер файлов игры')
    description = models.TextField(verbose_name='Описание')
    age_limited = models.BooleanField(default=False, verbose_name='Ограничение возраста 18+')
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

