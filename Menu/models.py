from django.db import models
from Auth.models import User
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu/')
    description = models.TextField()

       
    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'
        
    def __str__(self):
        return self.name    