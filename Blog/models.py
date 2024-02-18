from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.TextField( blank=False, default='')
    image = models.ImageField(upload_to='blog/')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField( null=True, unique=True)
    
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blog'
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        
        return reverse("detail_blog", kwargs={"slug": self.slug})

    
       