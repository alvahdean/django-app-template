from django import forms
from collection.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'url' ]


        

