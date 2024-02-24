from django.db import models
from Auth.models import User
from Menu.models import Menu
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200, null=True)
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )

    #created_at = models.DateTimeField(auto_add_now=True)
    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        
        
    def __str__(self):
        return self.title 
    