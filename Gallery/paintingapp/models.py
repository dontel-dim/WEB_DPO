from django.db import models
from django.urls import reverse

class Artist(models.Model):
    """Художники"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField('Описание')
    image = models.ImageField("Фото", upload_to='artist/')

    def __str__(self): 
        return self.name
    
    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'slug': self.name})
    
    class Meta: 
        verbose_name = "Художник" 
        verbose_name_plural = "Художники"


class Painting(models.Model):
    '''Картины'''
    title = models.CharField("Название", max_length=100)
    description = models.TextField('Описание')
    artist = models.ManyToManyField(Artist, verbose_name="художники", related_name="painting_artist")
    price = models.PositiveIntegerField('Цена', default=0, help_text="указывать сумму в рублях")
    image = models.ImageField("Картина", upload_to='painting/')
    slug = models.SlugField(unique=True, blank=True)
    phone_number = models.PositiveIntegerField("Номер телефона", max_length=11, blank=True, default=0)  

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self): 

        return reverse("painting_detail", kwargs={"slug": self.url}) 

    class Meta: 
        verbose_name = "Картина" 
        verbose_name_plural = "Картины"


# Create your models here.
