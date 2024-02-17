from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class User (AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
# class UserLoginCustom(UserCreationForm):
#     class Meta:
#         model = User  # Asegúrate de importar el modelo User
#         fields = ['username', 'password']

#     def __init__(self, *args, **kwargs):
#         super(UserLoginCustom, self).__init__(*args, **kwargs)

#         # Personaliza los widgets y agrega clases de CSS
#         self.fields['username'].widget.attrs.update({'class': 'tu-clase-css-username'})
#         self.fields['password'].widget.attrs.update({'class': 'tu-clase-css-password'})