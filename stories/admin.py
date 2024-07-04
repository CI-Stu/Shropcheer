from django.contrib import admin
from .models import Story
from .models import Comment

# Register your models here.
admin.site.register(Story)
admin.site.register(Comment)
