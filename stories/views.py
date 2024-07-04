from django.shortcuts import render
from django.views import generic
from .models import Story

# Create your views here.


class StoryList(generic.ListView):
    model = Story
