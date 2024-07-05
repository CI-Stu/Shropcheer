from django.contrib import admin
from .models import Story, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'body']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


# Register your models here.
admin.site.register(Comment)
