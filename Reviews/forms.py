from django import forms
from .models import Review

class ReviewForm(forms.Form):
    title = forms.CharField(
        label='title',
        required= True,
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'w-full rounded-md p-2 my-2', 'placeholder' : 'Nombre del comentario'}),
    )
    comment = forms.CharField(
        label='comment',
        required=True,
        max_length=500,       
        widget=forms.Textarea(attrs={'class' : 'w-full rounded-md p-2 my-2', 'placeholder' : 'Descripticion del comentario'})
    )
