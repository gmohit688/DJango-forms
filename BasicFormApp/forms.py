from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["username", "gender", "text"]
    
    def clean(self):
        super(PostForm, self).clean()
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')
        if len(username) < 5:
            self._errors['username'] = self.error_class(['Minimum 5 chars required'])
        if len(text) < 10:
            self._errors['text'] = self.error_class(['Post Should Contain a minimum of 10 characters'])
        return self.cleaned_data


