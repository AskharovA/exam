from django.forms import ModelForm, CharField, TextInput
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post
from taggit.forms import TagWidget, TagField


class CommentForm(ModelForm):
    body = CharField(required=True, widget=SummernoteWidget(attrs={
        'summernote': {
            'width': '100%',
            'height': '400px',
        }
    }))

    class Meta:
        model = Comment
        fields = ['body']


class PostForm(ModelForm):
    title = CharField(required=True, widget=TextInput(attrs={
        'class': 'form_input',
        'autocomplete': 'off',
    }))
    body = CharField(required=True, widget=SummernoteWidget(attrs={
        'summernote': {
            'width': '100%',
            'height': '500px',
        }
    }))
    tags = TagField(required=False, widget=TagWidget(attrs={
        'class': 'form_input',
    }))

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'tags',
            'category',
        ]
