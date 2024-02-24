from audioop import reverse
from django.db import models
from Auth.models import User
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu/')
    description = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    
    
       
    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'
        
    def __str__(self):
        return self.name    
    
    def get_absolute_url(self):
        return reverse("menu_detail", kwargs={"slug": self.slug})
    