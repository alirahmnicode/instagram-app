from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('descriptions','image',)



class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('descriptions','image',)



