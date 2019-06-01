from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
   class Mate:
      model = Blog
      fields = ['title','body']