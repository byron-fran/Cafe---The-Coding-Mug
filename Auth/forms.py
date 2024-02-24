from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',       
        widget=forms.EmailInput(attrs={'class': 'w-full border border-gray-300 rounded-md text-black', 'placeholder' : 'example@gmail.com'} ),
      
        
    )
    
    password1 = forms.CharField(
        label="Password",
        
        widget=forms.PasswordInput(attrs={'class': 'w-full border border-gray-300 rounded-md text-black'}),
        
    )
    
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'w-full border border-gray-300 rounded-md text-black'}),

    )
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md text-black', 'placeholder' : 'Write your name'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')