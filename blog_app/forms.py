from django import forms
from .models import Post, Tag
from django.forms import ModelForm

class PostAddForm(forms.ModelForm):    
   class Meta:
       model = Post
       fields = ['title', 'text', 'image', 'tag']
