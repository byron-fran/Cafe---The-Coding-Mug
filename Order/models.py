from django.db import models
from Auth.models import User
from Menu.models import Menu
# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='orders/')
    description = models.TextField()
    quantity = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        
    def __str__(self):
        return self.name    