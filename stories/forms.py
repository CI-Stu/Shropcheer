from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Story


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class StoryForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Story
        fields = [
            'title',
            'body',
            'image',
            'story_location',
            'news_category',
            ]

        labels = {
            'title': 'Story Headline',
            'body': 'Story Text',
            'image': 'Story Image',
            'story_location': 'Location',
            'news_category': 'Category',
        }
